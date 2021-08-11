import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

st.title("OCR")

st.markdown("## Optical Character Recognition")

st.markdown("")

image = st.file_uploader(label = "Please upload your image",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en','th'],model_storage_directory='.')
    return reader 

reader = load_model()

if image is not None:

    input_image = Image.open(image)
    st.image(input_image)

    with st.spinner("🤖 is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = []


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    st.success("Here you go!")
else:
    st.write("Upload an Image")




