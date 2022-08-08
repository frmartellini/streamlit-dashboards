import pandas as pd
import plotly.express as px
import streamlit as st

# Para rodar o streamlit no terminal
# streamlit run nomeCodigo.py

# Read dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Rename columns
df = df.rename(columns={'newDeaths': 'Novos Óbitos', 'newCases': 'Novos Casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

# Select state
states = list(df['state'].unique()) # list all states
select_uf = st.sidebar.selectbox('Qual estado?', states)
# state = 'SP' # get one state only

# Select Column
# col = 'Casos por 100 mil habitantes' # get one column only
cols = ['Novos Óbitos','Novos Casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes'] # get more than one colum
select_cols = st.sidebar.selectbox('Qual é o tipo de informação?', cols)

# Select the line to the selected state
df = df[df['state'] == select_uf]

fig = px.line(df, x='date', y=select_cols, title=select_cols + ' - ' + select_uf)
fig.update_layout(xaxis_title='Data',yaxis_title=select_cols.upper(), title={'x':0.5})

st.title('DADOS COVID - BRASIL') # não coloco sidebar porque quero que o título fique na página principal
st.write('Escolha o estado e o tipo de informação para mostrar o gráfico, no menu lateral')
# print('DADOS COVID - BRASIL')
# print('Escolha o estado e o tipo de informação para mostrar o gráfico, no menu lateral')

st.plotly_chart(fig, use_container_width=True) # mostra o gŕafico no streamlit
# fig.show() # vai mostrar dentro do código python

st.caption('Fonte dos dados: Número de casos confirmados de COVID-19 no Brasil - https://github.com/wcota/covid19br')
# print('Fonte dos dados: Número de casos confirmados de COVID-19 no Brasil - https://github.com/wcota/covid19br')