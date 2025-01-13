import streamlit as st
from transformers import pipeline
from PIL import Image

caption=pipeline('image-to-text',model='ydshieh/vit-gpt2-coco-en')
uploaded_image=st.file_uploader("upload an image", type=["png","jpg","jpeg"])
if uploaded_image is not None:
    Image=Image.open(uploaded_image)
    st.image(Image, caption="uploaded_image", use_column_width=True)
    if st.button("Generate caption"):
        captions=caption(Image)
        st.write(captions[0],['generated text'])
