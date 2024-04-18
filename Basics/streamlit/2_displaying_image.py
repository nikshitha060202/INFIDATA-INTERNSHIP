import streamlit as st
from PIL import Image
img=Image.open('test.jpg')
st.title('DISPLAYING IMAGE')
st.image(img,width=250)

st.header('this is image')
img2=Image.open('butterfly.jpg')
st.title('DISPLAYING IMAGE')
st.image(img2,width=750)