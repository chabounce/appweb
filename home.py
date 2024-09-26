import streamlit as st

#Titre
st.title("Mon formulaire")

#Texte
st.write("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input("Tapez votre texte :")

st.write(user_input)

#Image
st.image("https://fac.img.pmdstatic.net/fit/~1~fac~2021~12~20~db44c7df-7828-498b-821f-4bd03cdfb75d.jpeg/1200x900/quality/80/crop-from/center/tout-savoir-sur-l-orque.jpeg")

#Sidebar
st.sidebar.title("Charlotte Jeun")

#Video dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=1laVrla1T_U")

#Select Bar
student_grad = st.selectbox("Sélectionnez votre niveau d'études",["Bac","Bac +2","Bac +5"])

#Select slider
age = st.select_slider("Quel est votre âge ?", range(0,99))

if age > 18 :
    st.write("Vous êtes majeur")
