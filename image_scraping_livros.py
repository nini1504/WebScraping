import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

os.makedirs("Images", exist_ok=True)

url = "https://books.toscrape.com/"

resposta = requests.get(url)
print(resposta)
i = 1

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, "html.parser")
    # print(soup.prettify())

    capas_livros = soup.find_all('img')
    # print(capas_livros)

    for img in capas_livros:
        print("Imagem", i, img["src"])
        i += 1

        path = img.get("src") #aqui ainda é string
        url_completa = urljoin(url, path) #junta a url da pagina com o caminho da imagem
        # print(url_completa)

        imagem = requests.get(url_completa).content #recebe uma sequência de bits
        # print(imagem)

        with open(f"Images/imagem_{i}.jpg", "wb") as f:    # cria um arquivo dentro da pasta Imagens, com nome imagem_i.jpg
            f.write(imagem) #cria a imagem, "escreve ela a partir do binario"

    print("Imagens baixadas com sucesso")

    # # ATIVIDADE PROPOSTA: salvar as iamgens com o nome do livro