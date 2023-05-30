import time
import streamlit as st

st.image('logo.png', width=250)
st.header('Bem-vindo ao nosso sistema!')
st.text('Faça o upload de uma foto para identificação automatizada de segurança!')

upload_file = st.file_uploader("Escolha uma foto")

isSecurity = False

if upload_file is not None:
  with st.spinner('Carregando...'):
    time.sleep(5)

  st.image(upload_file, width=350)

  if isSecurity: 
    st.success('Todos procedimentos de segurança respeitados!', icon="✅")
  else:
    st.error('Procedimento de segurança burlado!! Atenção!', icon="🚨")

