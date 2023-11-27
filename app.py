import streamlit as st
from text_model import Models
import os

st.title("Story Teller")
model = Models()
st.write("Upload an image and get a story")
uploaded_file = st.file_uploader("Upload your file here...",type=['png','jpeg','jpg'])

try:
    if uploaded_file is not None:
        st.image(uploaded_file)
        with open(os.path.join("images",uploaded_file.name),"wb") as f: 
            f.write(uploaded_file.getbuffer()) 
        response = model.chain(model.img2text(f'images/{uploaded_file.name}'))
        st.write(response)
except Exception as e:
    print(e)
    st.write("error occured! please try again")
