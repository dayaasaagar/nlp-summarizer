# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:00:37 2022

@author: dayaaasaagar
"""

import streamlit as st 
from eng_sum import input_url
from PIL import Image
from bert_summ import bert_sum
from hindi_summ import hindi_tokenize
image = Image.open('maxresdefault.jpg')

st.image(image, caption='123')
#from bert_summ import bert_sum
st.title('News text summarizer')

st.sidebar.title("News Summarization Web App")
option = ["English", "Hindi"]

choice = st.sidebar.selectbox("Select of your choice", options=option)

if choice =="English":
    link=st.text_input("enter the news article")
    if st.button("Summarize"):
        input_url(link)
    if st.button("bert"):
        bert_sum(link)
if choice =="Hindi":
    text=st.text_area("enter the news article")
    if st.button("Summarize"):
        hindi_tokenize(text)

        
    
    
