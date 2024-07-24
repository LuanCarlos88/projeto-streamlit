import streamlit as st
import pandas as pd

dados = pd.read_csv('Clientes.csv')

st.title('Clientes cadastrados')
st.divider()

st.dataframe(dados)

