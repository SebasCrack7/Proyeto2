import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

apgn = pd.read_csv("datos_anteproyecto1.csv")
ran = pd.read_csv("datos_random.csv")

st.title("Aplicación 2")

tab1, tab2 = st.tabs(["Tab1","Tab2"])



with tab1:
    
    #análisis univariado
    fig, ax=plt.subplots(1,3, figsize=(10,4))
    #educ
    tab_freq = ran["educacion"].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values)
    #edad
    ax[1].hist(ran["edad"], bins=30)  #Numero de intervalos
    #wage
    ax[2].hist(ran["salario"], bins=40)
    st.pyplot(fig)
    #anális bivariado
    fig, ax = plt.subplots(1,2, figsize=(10,4))
    #educ vs wage
    ax[0].scatter(ran["educacion"], ran["salario"])
    #edad vs wage
    ax[1].scatter(ran["edad"], ran["salario"])

    st.pyplot(fig)

with tab2:
    fig = px.treemap(data_frame = apgn, path=[px.Constant("PGN"),"Nombre Sector","Tipo de gasto"],values="Valor")
    st.plotly_chart(fig)