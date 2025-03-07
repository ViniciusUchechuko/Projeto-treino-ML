import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('pizzas.csv')

modelo = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)


st.title('Prevendo o Valor de uma Pizza')
st.divider()

diametro = st.number_input('Digite um número:', value=None, placeholder='Digite o tamanho do diametro da pizza')


if diametro:

    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'O valor de uma pizza com diâmetro de {diametro:.2f} cm é de {preco_previsto:.2f} R$')
    st.balloons()
