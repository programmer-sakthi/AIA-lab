#experiment 1

from textblob import TextBlob
from textblob.en import polarity

# Sentiment Analysis
text = "I want to kill myself"
analysis = TextBlob(text)
polarity=analysis.sentiment.polarity
print(polarity)



if polarity>0:
    print("Positive")
elif polarity==0:
    print("Neutral")
else:
    print("Negative")





