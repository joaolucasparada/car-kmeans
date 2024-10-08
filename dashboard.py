import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

st.set_page_config(layout='wide')

st.title(':car: Correlação | PCA | K-Means')

data0 = pd.read_csv('data0.csv')
data1= pd.read_csv('data1.csv')
datadict = pd.read_csv('datadict.csv', sep=';', encoding='latin1')
projection = pd.read_csv('projection.csv')

fig = px.imshow(data1.corr().round(2), color_continuous_scale='plasma', text_auto=True)
fig.show()

col1, col2 = st.columns(2)
con2 = col2.container(border=True)

col1.write('Dicionário de Dados: ')
col1.dataframe(datadict)

con2.write('Matriz de correlação: ')
fig = px.imshow(data1.corr().round(2), color_continuous_scale='plasma', text_auto=True)
con2.plotly_chart(fig)

col3, col4 = st.columns([2, 2])
col3.write('K-Means clusters:')
fig1 = px.strip(projection, x='x',y='y',color='cluster_pca', color_discrete_sequence=['blue', 'yellow', 'orange', 'green', 'purple'],  hover_data=['x', 'y', 'Car', 'Year'])
col3.plotly_chart(fig1)
col4.metric(label='Variance Ratio', value='59%')
col4.metric(label='Variance', value='4.75')


