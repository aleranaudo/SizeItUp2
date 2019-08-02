'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
polarity = []
subjectivity = []
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
tb = TextBlob("d o m i n i c!")
print(tb)
print(tb.polarity)
print(tb.subjectivity)
polarity.append(tb.polarity)
subjectivity.append(tb.subjectivity)

import math
Sum = sum(subjectivity)
average = Sum/len(subjectivity)
print("average subjectivity", average)

print(polarity, subjectivity)

Sum = sum(polarity)
average = Sum/len(polarity)
print("average polarity", average)
