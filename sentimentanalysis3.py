# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:44:30 2018

@author: Zeus-pc
"""

##import nltkfrom nltk.sentiment.vader
##import SentimentIntensityAnalyzer
##nltk.download('vader_lexicon’)


import os
os.chdir(“C:/texts”)
import glob as glob
files = glob.glob(“.txt”) #files will be a list of all txt files
documents = [] #list of contents of each txt file
for f in files:
      with open(f) as infile:
	txt = infile.read()
	documents.append(txt)


