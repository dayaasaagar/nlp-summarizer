# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:22:00 2022

@author: dayaaasaagar
"""
import streamlit as st
import requests
def bert_sum(news_url):
    
    json_body = {
        "url": news_url
            }

    resp = requests.post("https://api.smrzr.io/v1/summarize/news?num_sentences=5&min_length=40", json=json_body).json()
    summary = resp['summary']
    st.write("    ")
    st.write("summary using bert",summary)