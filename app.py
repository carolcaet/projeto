import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np

car_data = pd.read_csv('vehicles.csv')

st.header('Dados dos veículos')

car_data = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

hist_button = st.button('Criar histograma') 
     
if hist_button: 
    st.write('Histograma para o conjunto de dados de anúncios de vendas de carros')
         
    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão')

if disp_button:
    st.write('Gráfico de dispersãopara o conjunto de dados de anúncios de vendas de carros')
    
    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
    