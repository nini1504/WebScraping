import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://itforum.com.br/noticias/gptw-melhores-empresas-ti-2025/'

resposta = requests.get(url)
print(resposta)

all_empresas = []

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.content, 'html.parser')
    inicio_captura = soup.find('h2', string=lambda t: t and 'Grandes empresas' in t)

    if inicio_captura:
        listas_empresas = inicio_captura.find_all_next('ol')
        for lista in listas_empresas:
            itens = lista.find_all('li')
            for i in itens:
                all_empresas.append(i.get_text(strip=True))

    print(all_empresas)

    # Para salvar no Excel
    posicoes = []
    nomes = []

    for i, nome in enumerate(all_empresas, start=1):
        posicoes.append(f"{i}º")
        nomes.append(nome)

    df = pd.DataFrame({
        'Ranking': posicoes,
        'Nome da Empresa': nomes
    })
  
    df.to_excel('ranking_empresas_completo.xlsx', index=False)
      
    print("Planilha criada.")
