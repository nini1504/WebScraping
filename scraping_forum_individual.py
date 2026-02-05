import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://itforum.com.br/noticias/gptw-melhores-empresas-ti-2025/'

resposta = requests.get(url)
print(resposta)

empresas = []

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.content, 'html.parser')
    titulo = soup.find('h2', string=lambda t: 'Grandes empresas' in t)

    if titulo:
        lista_grandes_empresas = titulo.find_next('ol')
        if lista_grandes_empresas:
            lista = lista_grandes_empresas.find_all('li')
            for i in lista:
                empresas.append(i.get_text(strip=True))
                
    print(empresas)

    # Para salvar no Excel
    posicoes = []
    nomes = []

    for i, nome in enumerate(empresas, start=1):
        posicoes.append(f"{i}º")
        nomes.append(nome)

    df = pd.DataFrame({
        'Ranking': posicoes,
        'Nome da Empresa': nomes
    })
  
    df.to_excel('ranking_empresas_2.xlsx', index=False)
      
    print("Planilha criada.")
