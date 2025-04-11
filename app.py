import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt 
import plotly.express as px

apgn = pd.read_csv('datos_anteproyecto.csv')
ran = pd.read_csv('datos_random.csv')

st.title("Aplicacion 2")

tab1, tab2 = st.tabs(['Tab 1', 'Tab2'])

with tab1:
    #análisis univariado
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))
    # educ
    tab_freq = ran['educ'].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values, color='skyblue')
    # edad
    ax[1].hist(ran['edad'], bins=30, color='lightgreen', edgecolor='black')
    # wage
    ax[2].hist(ran['wage'], bins=40, color='salmon', edgecolor='black')

    st.pyplot(fig)

    ##análisis bivariado 
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    #educ vs. wage 
    ax[0].scatter(ran['educ'], ran['wage'], color='#8E44AD', alpha=0.7, edgecolor='black')
    #edad vs. wage
    ax[1].scatter(ran['edad'], ran['wage'], color='#E67E22', alpha=0.7, edgecolor='black')
    
    st.pyplot(fig)

with tab2:
    fig = px.treemap(data_frame=apgn,
           path=[px.Constant("PGN"),
                 "Nombre Sector",
                 "Tipo de gasto"],
           values='Valor',
           color='Valor',
           color_continuous_scale=px.colors.sequential.Agsunset)

    st.plotly_chart(fig)