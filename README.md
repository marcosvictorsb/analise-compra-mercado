# Projeto de Extração de Produtos de Compras no Amantino

Este é um projeto em Python desenvolvido com o objetivo de acessar o site do Amantino e extrair informações sobre todos os produtos disponíveis para compra.

## Descrição

O objetivo principal deste projeto é automatizar o processo de coleta de informações sobre as compras realizadas no site do Amantino, um supermercado que oferece uma variedade de produtos. Utilizando técnicas de web scraping, o programa acessará os pedidos já realizados no site, extrairá os produtos e armazenará essas informações para uso posterior.

## Funcionalidades

- Acesso automatizado ao site do Amantino.
- Coleta de informações sobre as compras realizadas.
- Armazenamento dos dados em um arquivo CSV para análise posterior.

## Como Usar

1. Certifique-se de ter o Python [instalado](https://www.python.org/downloads/) em seu sistema.
2. Clone este repositório: `git clone git@github.com:marcosvictorsb/analise-compra-mercado.git`
3. Acesse o diretório do projeto: `cd analise-compra-mercado`
4. Crie e ative um ambiente virtual:
   - `python -m venv nome_do_ambiente`
   - Ativando o ambiente virutal no Windows: `nome_do_ambiente\Scripts\activate`
   - Ativando o ambiente virutal no macOS/Linux: `source nome_do_ambiente/bin/activate`
5. Instale as dependências necessárias: `pip install -r requirements.txt`
6. Renomeio o arquivo `.env.example` para `.env` e insira seu e-mail e senha nas variaveis presente nesse arquivo.
7. Execute o script principal: `python main.py`

## Requisitos

- Python 3.x
- Bibliotecas listadas em `requirements.txt`

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Aviso Legal

Este projeto foi criado apenas para fins educacionais e de aprendizado. Certifique-se de estar em conformidade com os termos de uso do site Amantino ao utilizar este script.
