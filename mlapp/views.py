from django.shortcuts import render
from textblob import TextBlob

def index(request):
    print("it will come in the view function#########################################", type(request.method))

    result = None  # Initialize result to None

    if request.method == "POST":
        print("yes it comes")
        userdata = request.POST.get('user_input')
        print("user_input", userdata)

        # Create a TextBlob object
        blob = TextBlob(userdata)

        # Get sentiment polarity (ranges from -1 to 1, where negative values indicate negative sentiment)
        sentiment_score = blob.sentiment.polarity

        # Classify sentiment based on the score
        if sentiment_score > 0:
            result = 'Positive'

        elif sentiment_score < 0:
            result = 'Negative'
            
        else:
            result = 'Neutral'

    return render(request, 'home.html', {'result': result})
