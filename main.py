import streamlit as st
from transformers import pipeline
from PIL import Image
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    '''
    caption=pipeline('image-to-text',model='ydshieh/vit-gpt2-coco-en')
    uploaded_image=st.file_uploader("upload an image", type=["png","jpg","jpeg"])
    if uploaded_image is not None:
        image=Image.open(uploaded_image)
        st.image(image, caption="uploaded_image", use_column_width=True)
        if st.button("Generate caption"):
            captions=caption(image)
            st.write(captions[0],['generated text'])
    '''
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, port=8081)
