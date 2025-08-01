import pandas as pd
import plotly.express as px
import streamlit as st
     
st.header('Datos sobre la venta de coches')
car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir dispersion')
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el boton
    # escribir un mensaje
    st.write('Creación de dispersion para el conjunto de datos de anuncios de venta de coches') 

    # crear grafica de disperion 
    fig = px.scatter(car_data, x="odometer", y="price")  

    # mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)  