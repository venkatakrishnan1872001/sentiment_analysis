# # # import nltk

# # # # Download the VADER lexicon if not already downloaded
# # # try:
# # #     nltk.data.find('sentiment/vader_lexicon.zip')
# # # except LookupError:
# # #     nltk.download('vader_lexicon')

# # # # Continue with your code
# # # from nltk.sentiment import SentimentIntensityAnalyzer

# # # def analyze_sentiment(request):

# # #     print("Function is called")
# # #     if request.method == 'POST':
# # #         user_input = request.POST['user_input']
        
# # #         # Sentiment analysis using NLTK
# # #         sia = SentimentIntensityAnalyzer()
# # #         sentiment_score = sia.polarity_scores(user_input)['compound']

# # #         # Classify sentiment based on the score
# # #         if sentiment_score >= 0.05:
# # #             result = 'Positive'
# # #         elif sentiment_score <= -0.05:
# # #             result = 'Negative'
# # #         else:
# # #             result = 'Neutral'

# # #         return render(request, 'index.html', {'result': result})

# # #     print("Function ended")
# # #     return render(request, 'index.html')


# # from textblob import TextBlob

# # def analyze_sentiment(text):
# #     # Create a TextBlob object
# #     blob = TextBlob(text)

# #     # Get sentiment polarity (ranges from -1 to 1, where negative values indicate negative sentiment)
# #     sentiment_score = blob.sentiment.polarity

# #     # Classify sentiment based on the score
# #     if sentiment_score > 0:
# #         return 'Positive'
# #     elif sentiment_score < 0:
# #         return 'Negative'
# #     else:
# #         return 'Neutral'

# # # Example usage
# # user_input = "you saddist"
# # result = analyze_sentiment(user_input)
# # print(result)

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# from sklearn import metrics
# from sklearn.pipeline import make_pipeline


# # Sample data (replace this with your labeled dataset)
# texts = ["I love this product!", "This is terrible.", "Neutral statement."]
# labels = ["positive", "negative", "neutral"]

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# # Create a pipeline with TfidfVectorizer and Multinomial Naive Bayes classifier
# model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# # Train the model
# model.fit(X_train, y_train)

# # Predict on the test set
# predictions = model.predict(X_test)

# # Evaluate the performance
# accuracy = metrics.accuracy_score(y_test, predictions)
# print(f"Accuracy: {accuracy:.2f}")

# # Example usage for new text
# new_text = "This is a great experience!"
# prediction = model.predict([new_text])
# print(f"Predicted sentiment for '{new_text}': {prediction[0]}")


################  downloading dataset for analysis ################################

# import nltk
# from nltk.corpus import movie_reviews

# nltk.download('movie_reviews')

# nltk.download('punkt')

# # Get the file IDs for positive and negative reviews
# positive_fileids = movie_reviews.fileids('pos')
# negative_fileids = movie_reviews.fileids('neg')

# # Read the positive and negative reviews
# positive_reviews = [movie_reviews.raw(fileid) for fileid in positive_fileids]
# negative_reviews = [movie_reviews.raw(fileid) for fileid in negative_fileids]

# # Create labels for the reviews (1 for positive, 0 for negative)
# positive_labels = [1] * len(positive_reviews)
# negative_labels = [0] * len(negative_reviews)

# # Combine the reviews and labels
# reviews = positive_reviews + negative_reviews
# labels = positive_labels + negative_labels

# print("Dataset downloaded successfully!")
