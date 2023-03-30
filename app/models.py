from django.db import models
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('certificate', args=[str(self.id)])

class Certificate(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    certificate = models.ImageField(upload_to='certificates')

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} certificate'

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'id': 'firstName'})
        self.fields['middle_name'].widget.attrs.update({'class': 'form-control', 'id': 'middleName'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'id': 'lastName'})
        self.fields['department'].widget.attrs.update({'class': 'form-control', 'id': 'department'})
        self.fields['year'].widget.attrs.update({'class': 'form-control', 'id': 'year'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'id': 'year'})
    class Meta:
        model = Student
        fields = ("__all__")
