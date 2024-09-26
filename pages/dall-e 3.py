import streamlit as st

st.title("Dall-e 3")

user_input = st.text_input("Application Web - Open IA")
st.write(user_input)

sidebar_input = st.sidebar.text_input("Tapez votre texte ici :")
st.write(sidebar_input)

from openai import OpenAI
client = OpenAI(api_key=OpenAIKEY)

prompt = "A cute baby sea otter"

image = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url

st.image_url
