# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 07:10:40 2022

@author: dayaaasaagar
"""
#import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import math
import re
import indicnlp
import indicnlp.tokenize.sentence_tokenize
from heapq import nlargest
import streamlit as st 
def hindi_tokenize(text):
    tokens = word_tokenize(text)
    hindi_stop_words = ['अत','अपना','अपनी','अपने','अभी','अंदर','आदि','आप','इत्यादि','इन ','इनका','इन्हीं','इन्हें','इन्हों','इस','इसका','इसकी','इसके','इसमें','इसी','इसे','उन','उनका','उनकी','उनके','उनको','उन्हीं','उन्हें','उन्हों','उस','उसके','उसी','उसे','एक','एवं','एस','ऐसे','और','कई','कर','करता','करते','करना','करने','करें','कहते','कहा','का','काफ़ी','कि','कितना','किन्हें','किन्हों','किया','किर','किस','किसी','किसे','की','कुछ','कुल','के','को','कोई','कौन','कौनसा','गया','घर','जब','जहाँ','जा','जितना','जिन','जिन्हें','जिन्हों','जिस','जिसे','जीधर','जैसा','जैसे','जो','तक','तब','तरह','तिन','तिन्हें','तिन्हों','तिस','तिसे','तो','था','थी','थे','दबारा','दिया','दुसरा',
'दूसरे','दो','द्वारा','न','नके','नहीं','ना','निहायत','नीचे','ने','पर','पहले','पूरा','पे','फिर','बनी','बही','बहुत','बाद','बाला','बिलकुल','भी','भीतर','मगर','मानो','मे','में','यदि','यह','यहाँ','यही','या','यिह','ये','रखें','रहा','रहे','ऱ्वासा','लिए','लिये','लेकिन','व','वग़ैरह','वर्ग','वह','वहाँ','वहीं','वाले','वुह','वे','सकता','सकते','सबसे','सभी','साथ','साबुत','साभ','सारा','से','सो','संग','ही','हुआ','हुई','हुए','है','हैं','हो',
'होता','होती','होते','होना','होने','मैंने']
    stop_words = hindi_stop_words
    stop = [w for w in stop_words if w in tokens]  
    filtered_sentence = [w for w in tokens if not w in stop_words]
    words=' '.join(filtered_sentence)
    filtered_sentences=punctuate_sentences(words)
    word_frequencies = {}
    for word in tokens:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency
    sent_token = indicnlp.tokenize.sentence_tokenize.sentence_split(text,lang="Hi")
    sentence_scores = {}
    for sent in sent_token:
        sentence = sent.split(" ")
        for word in sentence:        
            if word.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.lower()]
    select_length = int(len(sent_token)*0.3)
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
    final_summary = [word for word in summary]
    summary = ' '.join(final_summary)
    st.write("   ")
    st.write("Summary from the site is ",summary)
    
    
                    
    
    
    
def punctuate_sentences(x):
    text = re.sub(r'(\d+)', r'',x)
    text = text.replace('\n', '')
    text = text.replace(u',', '')
    text = text.replace(u'"', '')
    text = text.replace(u'(', '')
    text = text.replace(u')', '')
    text = text.replace(u'"', '')
    text = text.replace(u':', '')
    text = text.replace(u"'", '')
    text = text.replace(u"’", '')
    text = text.replace(u"‘", '')
    text = text.replace(u"‘‘", '')
    text = text.replace(u"’’", '')
    text = text.replace(u"''", '')
    text = text.replace(u".", '')
    text = text.replace(u'?', u'।')
    sentences = text.split(u"।")
    return sentences
