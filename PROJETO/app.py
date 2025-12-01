import pandas as pd 
import streamlit as st 
import plotly.express as px 

#TITULOS  
st.title("II SIMPÓSIO CIENTÍFICO DO DCET - UNIFAP ")
st.subheader("Vizualização de dados de queimadas - Fonte: INPE")

#DEFINIÇÃO DE UMA SIDE BAR
dados = st.sidebar.selectbox('Selecione a data', ['2025-11-25','2025-11-26','2025-11-27','2025-11-28','2025-11-29','2025-11-30'])