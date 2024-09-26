import streamlit as st

st.title("Dall-e 3")

#Champ de saisie
user_input = st.text_input("Application Web - Open IA")
st.write(user_input)

#Champ de saisie dans la sidebar (pour la clé OpenAI)
sidebar_input = st.sidebar.text_input("Tapez la clé OpenAI ici :")
st.write(sidebar_input)

#Intéraction avec OpenAI
from openai import OpenAI
client = OpenAI(api_key=sidebar_input)

prompt = "A cute baby sea otter"

image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url

#Affichage de l'image
st.image(image_url)
