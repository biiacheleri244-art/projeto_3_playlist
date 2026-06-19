import streamlit as st
import json
#carregando arquivo .json
with open("playlist.json", "r", encoding= 'utf-8') as arquivo:
    dados = json.load(arquivo)

#--------------------------SIDEBAR
st.sidebar.title("MinhaFita")
# st.sidebar.image("")

estilo = st.sidebar.selectbox(" EScolha um estilo músical:", dados['estilos'].keys())
artista = st.sidebar.selectbox("Escolha um artista:", dados ['estilos'][estilo]['Artistas'].keys())

#------------------------------BODY
st.title(artista)

video, sobre = st.tabs(["Vídeo","Sobre"])

with video:
    st.video(dados['estilos'][estilo]['Artistas'][artista]['video'])

with sobre:
    nome_arquivo = dados['estilos'][estilo]['Artistas'][artista]['sobre']

    with open (nome_arquivo, 'r', encoding='utf-8') as arquivo:
       texto = arquivo.read()

    st.markdown(texto)