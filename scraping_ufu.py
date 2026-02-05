import requests
from bs4 import BeautifulSoup

resposta = requests.get('https://ufu.br/')
print(resposta)
# print(resposta.url)
# print(resposta.status_code)
# print(resposta.content)

if(resposta.status_code == 200):
    soup = BeautifulSoup(resposta.content, 'html.parser')
    # print(soup.prettify())
    # print(soup.title.contents)
    linhas_barra_esquerda = soup.find('ul', class_ = "sidebar-nav nav-level-0")
    # print(menu_hamburguer)
    
    # lista_menu = menu_hamburguer.find_all('li', class_ = 'nav-item')
    # for linha in lista_menu:
    #     print(linha.text.strip())
        
    iniciar_captura = False
    linhas_desejadas_barra_esquerda = []
    for li in linhas_barra_esquerda:
        if 'Graduação' in li.text.strip():
            iniciar_captura = True
        if iniciar_captura:
            linhas_desejadas_barra_esquerda.append(li.text.strip())
    print(linhas_desejadas_barra_esquerda)
