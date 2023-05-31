import time
import streamlit as st

st.image('logo.png', width=250)
st.header('Bem-vindo ao nosso sistema!')
st.text('Faça o upload de uma foto para identificação automatizada de segurança!')

tabImg, tabVideo, tabWebCam = st.tabs(["Imagem", "Vídeo", "Webcam"])

isSecurity = False

def statusMessage(status):
  if status: 
    st.success('Todos procedimentos de segurança respeitados!', icon="✅")
  else:
    st.error('Procedimento de segurança burlado!! Atenção!', icon="🚨")

def loading():
  with st.spinner('Carregando...'):
      time.sleep(5)

with tabImg:
  upload_file = st.file_uploader("Escolha uma foto")

  if upload_file is not None:
    loading()

    st.image(upload_file, width=350)
    statusMessage(True)

with tabVideo:
  upload_file = st.file_uploader("Escolha um vídeo")

  if upload_file is not None:
    loading()
    video_bytes = upload_file.read()
    st.video(video_bytes)

with tabWebCam:
  picture = st.camera_input("Tire uma foto")

  if picture:
    loading()
    st.image(picture)
