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



from faker import Faker
from mlapp.models import Employee
from rest_framework.response import Response


def AddData(request):

    for _ in range(30): 
         # Adjust the range based on how many records you want to insert

        fake = Faker()
        name = fake.name()

        age = fake.random_int(min=18, max=99)  # Adjust the age range as needed

        # Create and save a new instance of your model
        Employee.objects.create(name=name, age=age)


    return Response({"success":True})

from rest_framework.generics import ListAPIView
from .pagination import MyCustomPagination
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyCustomPagination



# views.py
from django.shortcuts import render
from .models import Employee

def test_view(request):
    empinstance = Employee.objects.get(id=61)
    return render(request, 'test.html', {'empinstance': empinstance})
