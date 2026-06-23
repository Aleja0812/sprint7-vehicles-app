import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Análisis de Vehículos Usados')

# Descripción
st.write(
    'Esta aplicación permite explorar un conjunto de datos de vehículos usados mediante gráficos interactivos. '
    'Puedes visualizar la distribución del kilometraje y analizar la relación entre el precio y el kilometraje.'
)

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Distribución del kilometraje')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre precio y kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)