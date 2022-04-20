# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:41:50 2022

@author: dayaaasaagar
"""
import streamlit as st 
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
sw=set(stopwords.words('english'))
from string import punctuation
from newspaper import Article
import spacy
from heapq import nlargest
from textblob import TextBlob


def input_url(url):
    toi_article = Article(url, language="en")
    toi_article.download()
    toi_article.parse()
    toi_article.nlp()
    text1=toi_article.text
    nlp=spacy.load('en_core_web_sm')
    doc= nlp(text1)
    tokens = [token.text for token in doc]
    punctuation1 = punctuation +'\n'
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in sw:
            if word.text.lower() not in punctuation1:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text]=1
                else:
                    word_frequencies[word.text]+=1
                    
    
    
    max_frequency= max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens=[sent for sent in doc.sents]
    sentence_scores={}
    for sent in sentence_tokens:
        for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent]=word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length = int(len(sentence_tokens)*0.3)
    summary =nlargest(select_length,sentence_scores,key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    st.write("summary of the given news article is ","\n",summary)
    st.write("Length of the orginal text","\n",len(text1))
    st.write("Lenght of the summary",len(summary))
    analysis = TextBlob(text1)
    st.write("polarity of the text",analysis.polarity)
    st.write(f'sentiment:{"positive" if analysis.polarity>0 else "negative" if analysis.polarity < 0 else "neutral"}')
    
#link=input("enter the news article")
#input_url(link)  
