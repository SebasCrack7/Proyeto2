import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

apgn = pd.read_csv("datos_anteproyecto1.csv")
ran = pd.read_csv("datos_random.csv")

st.title("Aplicación 2")

tab1, tab2 = st.tabs(["Tab1","Tab2"])



with tab1:
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))

    # educ
    tab_freq = ran["educacion"].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values, color='skyblue')  # Color personalizado

    # edad
    ax[1].hist(ran["edad"], bins=30, color='orange')  # Color personalizado

    # wage
    ax[2].hist(ran["salario"], bins=40, color='green')  # Color personalizado

    st.pyplot(fig)

    # análisis bivariado
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # educ vs wage
    ax[0].scatter(ran["educacion"], ran["salario"], color='purple')  # Color personalizado

    # edad vs wage
    ax[1].scatter(ran["edad"], ran["salario"], color='red')  # Color personalizado

    st.pyplot(fig)

with tab2:
    fig = px.treemap(
    data_frame=apgn,
    path=[px.Constant("PGN"), "Nombre Sector", "Tipo de gasto"],
    values="Valor",
    color="Tipo de gasto",  # Esto activa el color por categoría
    color_discrete_sequence=px.colors.qualitative.Pastel  # Paleta personalizada
)

    st.plotly_chart(fig)