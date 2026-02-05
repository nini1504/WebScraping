import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.linkedin.com/pulse/linkedin-top-companies-2025-10-melhores-empresas-de-u8rxc/'

# É necessario simular navegador real pq porque o LinkedIn bloqueia acessos de scripts automatizados
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
resposta = requests.get(url, headers=headers)
print(resposta)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.content, 'html.parser')
    
    lista_h2 = soup.find_all('h2')
    empresas = []
    iniciar_captura = False

    if lista_h2:
        for h2 in lista_h2:
            if 'Mercado Livre' in h2.text.strip():
                iniciar_captura = True
            if iniciar_captura:
                empresas.append(h2.text.strip())
    else:
        print("não encontrei h2.")

    empresas = empresas[:10]

    # Para salvar no Excel
    posicoes = []
    nomes = []

    for i in empresas:
        partes = i.split('.', 1)
        numero = partes[0].strip()
        nome = partes[1].strip()
        posicoes.append(f"{numero}º")
        nomes.append(nome)

    df = pd.DataFrame({
        'Ranking': posicoes,
        'Nome da Empresa': nomes
    })
  
    df.to_excel('ranking_empresas.xlsx', index=False)
      
    print("Não foi possivel salvar a planilha.")
