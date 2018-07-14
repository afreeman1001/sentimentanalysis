# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 08:50:29 2018

@author: Zeus-pc
"""

import nltk from nltk.sentiment.vader
import SentimentIntensityAnalyzer
nltk.download('vader_lexicon’)

s= "I like pie"
sid = SentimentIntensityAnalyzer()
sid.polarity_scores(s) 