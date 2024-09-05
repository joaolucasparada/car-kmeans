import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import streamlit as st

st.title(':car: Correlação | PCA | K-Means')

data0 = pd.read_csv('data0.csv')
data1= pd.read_csv('data1.csv')
datadict = pd.read_csv('datadict.csv', sep=';')
projection = pd.read_csv('projection.csv')

fig = px.imshow(data1.corr().round(2), color_continuous_scale='plasma', text_auto=True)
fig.show()

st.write('Dicionário de Dados: ')
st.dataframe(datadict)

st.write('Matriz de correlação: ')
fig = px.imshow(data1.corr().round(2), color_continuous_scale='plasma', text_auto=True)
st.plotly_chart(fig)

st.write('K-Means clusters:')
fig1 = px.strip(projection, x='x',y='y',color='cluster_pca', color_discrete_sequence=['blue', 'yellow', 'orange', 'green', 'purple'],  hover_data=['x', 'y', 'Car', 'Year'])
st.plotly_chart(fig1)

col1, col2 = st.columns([2,6])
col1.metric(label='Variance Ratio', value='59%')
col2.metric(label='Variance', value='4.75')
