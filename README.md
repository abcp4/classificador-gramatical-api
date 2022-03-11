# Classificador Gramatical 

Classificador gramatical para fins acadêmicos.

## Como executar este projeto?

1. Instale as dependências do projeto com o comando abaixo
    ```shell
    pip install -r requirements.txt
    ```
2. Instale o modelo de português do spacy
    ```shell
    python -m spacy download pt_core_news_lg
    ```
3. Em seguida execute o projeto com o streamlit
    ```shell
    streamlit run app/main.py
    ```
4. Pronto! A aplicação vai ficar disponível no endereço exibido no terminal, clique nele e experimente a aplicação.