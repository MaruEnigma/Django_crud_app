from django.db import models


# Define the Student model which will be used to create and manage student records in the database
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()

    # Method to return a string representation of the Student object
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
