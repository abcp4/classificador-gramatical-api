import streamlit as st
from tips import get_tip
from classification.classifier import get_classification
from annotated_text import annotated_text
import pandas as pd

#===========================================#
#                 SideBar                   #
#===========================================#
st.sidebar.title("📖 Classificador gramatical")
st.sidebar.markdown("Você pode escolher um das anotações abaixo:")

tagset = st.sidebar.selectbox("Qual você prefere?", ("Spacy","Bosque", "GSD", "Linguateca", "Macmorpho"))

# st.sidebar.markdown("## 🙏 Pedido:")
# st.sidebar.markdown((
#     "Enquanto nosso programa roda sua frase: "
#     "você pode clicar no botão **Recado**, temos uma mensagem para você!"
#     )
# )

# message = st.sidebar.button("Recado")
# if message:
#     st.sidebar.info(get_tip())

#===========================================#
#                 Main                      #
#===========================================#

desc = "Classificador gramatical para fins didáticos. Tenha acesso ao código [aqui](https://github.com/classificador-gramatical/classificador-gramatical)!"

st.info(get_tip())
st.title("Classificador Gramatical")
st.write(desc)
user_input = st.text_input("Informe o seu texto aqui:")


def split_given_size(a, size):
    return [a[i:i+size] for i in range(0,len(a),size)]

if st.button("Verificar") or user_input:
    tagged_words, frase_morph, tokens = get_classification(user_input)
    print('tags: ',tagged_words)
    if tagged_words:
        annotated_text(*tagged_words)

    st.markdown("# Análise morfológica")
    if st.button("Analisar"):
        for index, morph in enumerate(frase_morph):
            st.markdown(f"### {tokens[index]}")
            df = pd.DataFrame(morph, columns=["Categoria", "Tipo"])
            st.table(df)
