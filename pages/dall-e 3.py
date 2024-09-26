import streamlit as st

st.title("Dall-e 3")

user_input = st.text_input("Application Web - Open IA")
st.write(user_input)

sidebar_input = st.sidebar.text_input("Tapez votre texte ici :")
st.write(sidebar_input)
