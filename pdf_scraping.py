import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

os.makedirs("pdfs_2024", exist_ok=True)

url = "https://www.montecarmelo.mg.gov.br/diario-oficial"

resposta = requests.get(url)
print(resposta)
# print(resposta.content)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, "html.parser")

    ano_2026 = soup.find("span", string="2024")
    lista_pdfs = ano_2026.find_next("ul")

    links = lista_pdfs.find_all("a", href=True)
    print(links)
    
    for link in links:
        texto = link.text.strip()
        href = link["href"]

        pdf_url = urljoin(url, href) 

        print("Baixando:", texto)

        resposta_pdf = requests.get(pdf_url)

        nome_arquivo = texto.replace(" ", "_") + ".pdf"

        with open(f"pdfs_2024/{nome_arquivo}", "wb") as f:
            f.write(resposta_pdf.content)

print("Arquivos pdfs baixados.")

