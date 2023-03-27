from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    year = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])