import streamlit as st
import pandas as pd
from datetime import date 

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("Clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}\n")
        st.session_state['sucesso'] = True
    else:
        st.session_state['sucesso'] = False


st.set_page_config(
    page_title= "Cadastro de clientes",
    page_icon= '📖'
)

st.title('Cadastro de clientes')
st.divider()


nome = st.text_input('Digite o nome do cliente',
                     key='nome_cliente')
data_nasc = st.date_input('Data de nascimento',
                     format= 'DD/MM/YYYY')
tipo = st.selectbox('Tipo do cliente',
                    ['Pessoa Física', 'Pessoa jurídica'])

btn_cadastrar = st.button('Cadastrar', 
                          on_click= gravar_dados,
                          args = [nome, data_nasc, tipo])

if btn_cadastrar:
    if st.session_state['sucesso']:
        st.success('Cliente cadastrado com sucesso',
                   icon= '✅')
    else:
        st.error('Aconteceu algum erro, cliente não cadastrado.',
                 icon= '❌')

