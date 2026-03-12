#streamlit (interface gráfica)
#criar ambiente virtual - python -m venv .venv
#ativar o ambiente venv/Scripts/activate
#instalar o stremlit, pip install streamlit

# importar bibliotecas
import streamlit as st   # biblioteca para criar o site/interface
import pandas as pd      # biblioteca para trabalhar com tabelas (DataFrame)
import numpy as np       # biblioteca para trabalhar com números e cálculos

# título principal da página
st.title('Meu primeiro site streamlit')

# parágrafo simples na página
st.write('Conteúdo do meu site')

# criação de uma tabela usando pandas
df = pd.DataFrame({
    'coluna 1': [1, 2, 3, 4],     # primeira coluna da tabela
    'coluna 2': [10, 20, 30, 40]  # segunda coluna da tabela
})

# mostrar a tabela na página
st.write(df)

# mostrar uma imagem na página (usando um link da internet)
st.image('https://i.pinimg.com/236x/55/28/ec/5528ec196558ccfb6d80263d9a55ffb2.jpg')

# criar um campo que abre e fecha (expander)
with st.expander('Gatinho fofo'):   # título da aba que pode expandir
    st.write('Esse é um gatinho muito fofo!')  # conteúdo dentro do expander

# criar um cabeçalho
st.header('Bem vindo ao meu site')

# texto explicando a estrutura
st.write('Estrutura do meu site em streamlit')

# campo para o usuário digitar o nome
nome = st.text_input('Digite o seu nome:')

# se o usuário digitou algo
if nome:
    st.write(f'Olá {nome}!')  # mostrar mensagem personalizada
    st.text('Final da página')  # texto simples

# título da seção do contador
st.title('Contador de vida')

# verificar se a variável "count" existe na sessão
# O session_state é uma memória temporária da sessão do usuário.Ele guarda valores mesmo quando o script roda novamente.
#Aqui o programa pergunta:"Já existe uma variável chamada count guardada na sessão?"Se não existir, ele cria.
if 'count' not in st.session_state:
    st.session_state.count = 0  # iniciar contador em 0

# criar botão
if st.button('Clique para contar'):
    st.session_state.count += 1  # adicionar +1 ao contador quando clicar

# mostrar quantas vezes o botão foi clicado
st.write(f'O botão foi clicado {st.session_state.count} vezes')

# criar uma linha divisória na página
st.divider()
