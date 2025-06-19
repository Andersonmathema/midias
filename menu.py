import streamlit as st 
import pandas as pd 

# Configuração da página
st.set_page_config(
    page_title='Apresentação de dados Excel',
    page_icon='🙌',
)

st.write('# Bem vindo ao apresentador de dados')
st.write('## Tabela')

# Caminho onde está localizado o arquivo excel
caminho_arquivo_1 = './dados_teste.xlsx'

# Ler o arquivo excel com o pandas
df1 = pd.read_excel(caminho_arquivo_1)

# Apresentar o arquivo em pandas no streamlit
#st.dataframe(df1)

st.dataframe(pd.read_excel('./dados_teste.xlsx'))
