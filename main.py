import streamlit as st
import requests
import json
from fake_useragent import UserAgent

def google_suggest(keyword):
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    ua = UserAgent()
    headers = {"user-agent": ua.chrome}
    response = requests.get(url, headers=headers, verify=False)
    suggestions = json.loads(response.text)
    return suggestions[1]

st.title("Sugestões do Google")

# Entrada do usuário para o termo de pesquisa
pesquisar = st.text_input("Pesquisar:", value="Python")

# Sugestões de pesquisa do Google
suggestions = google_suggest(pesquisar)

# Exibição das sugestões na tabela do Streamlit
st.write("Sugestões:")
for word in suggestions:
    st.write(word)
