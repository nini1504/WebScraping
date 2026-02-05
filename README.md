# Web Scraping Collection 

Este repositório armazena uma coleção de scripts desenvolvidos para a extração automatizada de dados de diferentes plataformas web. O foco principal é a transformação de dados não estruturados da web em formatos organizados para análise, como planilhas Excel e DataFrames.

## 📌 Projetos em Destaque

* **LinkedIn Top Companies 2025**: Script para extração do ranking das 10 melhores empresas para desenvolver carreira, incluindo nomes e links de perfis[cite: 15].
* **GPTW IT Forum 2025**: Automação para capturar o ranking das melhores empresas de TI (Categorias: Grandes, Médias e Pequenas) diretamente de notícias do setor[cite: 25].

## 🛠️ Tecnologias e Bibliotecas
* **Python**: Linguagem base para todos os scripts.
* **BeautifulSoup4**: Utilizada para navegação e parsing da árvore HTML (DOM).
* **Requests**: Responsável pelas requisições HTTP e simulação de User-Agents para evitar bloqueios.
* **Pandas**: Manipulação de dados e exportação para arquivos `.xlsx` e `.csv`.

## 🚀 Como Executar
1. Instale as dependências:
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl googlesearch-python
   ```
2. Execute os códigos no terminal:
   ```bash
   python nome_do_arquivo.py
   ```
