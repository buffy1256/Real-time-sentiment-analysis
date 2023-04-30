#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.write("# Real Time Sentiment Analysis")

user_input = st.text_input("Please Enter Any Text 🙄: ")
nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write(" ")
elif score["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")


# In[ ]:




