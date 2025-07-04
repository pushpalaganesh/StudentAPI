from django.db import models


# Create your models here.
class Student(models.Model):
    Student_id = models.CharField(max_length=15)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Branch = models.CharField(max_length=100)
    Marks = models.IntegerField()

    def __str__(self):
        return self.Name
