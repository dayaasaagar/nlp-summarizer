# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:00:37 2022

@author: dayaaasaagar
"""

import streamlit as st 
from bert_summ import bert_sum
#image = Image.open('maxresdefault.jpg')

#st.image(image, caption='123')
#from bert_summ import bert_sum
st.title('News text summarizer')
link=st.text_input("enter the news article")
if st.button("bert-Summarize"):
    bert_sum(link)

        
    
    
