from faker import Faker
from mlapp.models import Employee

for _ in range(30):  # Adjust the range based on how many records you want to insert
    name = fake.name()
    age = fake.random_int(min=18, max=99)  # Adjust the age range as needed

    # Create and save a new instance of your model
    Employee.objects.create(name=name, age=age)

