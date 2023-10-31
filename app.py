import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np

car_data = pd.read_csv('vehicles.csv')

st.header('Dados dos veículos')
st.write('Tabela com as informações sobre os veículos')

st.dataframe(car_data, height=300)

st.write('Clique em um dos botões abaixo para observar os gráficos')

hist_button = st.button('Criar histograma') 
     
if hist_button: 
    st.write('Histograma para o conjunto de dados de anúncios de vendas de carros')
         
    fig = fig = px.histogram(car_data, x="odometer", nbins=20, text_auto=True)

    fig.update_layout(title='Distribuição do Odômetro', width=500, height=500)

    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão')

if disp_button:
    st.write('Gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    fig = px.scatter(car_data, x="odometer", y="price")

    fig.update_traces(marker=dict(size=8, line=dict(width=2, color='black')), selector=dict(mode='markers'))

    fig.update_layout(scattermode='group', title='Dispersão entre quilometragem e preço', width=500, height=500)

    st.plotly_chart(fig, use_container_width=True)