# simple sentiment analysis program

positive_words = ["good", "happy", "love", "great", "excellent", "awesome", "nice"]
negative_words = ["bad", "sad", "hate", "terrible", "awful", "poor", "worst"]

print("Simple Sentiment Analysis Program")
print("----------------------------------")

# take user input
text = input("Enter a sentence: ").lower()

# counting matches
pos_count = 0

neg_count = 0

for word in positive_words:
    if word in text:
        pos_count += 1

for word in negative_words:
    if word in text:
        neg_count += 1

# decision
if pos_count > neg_count:
    print("Sentiment: Positive")
elif neg_count > pos_count:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
