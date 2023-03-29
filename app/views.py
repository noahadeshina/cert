from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, StudentForm
from django.contrib.auth.mixins import LoginRequiredMixin

# your view goes here

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students.html'

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_detail.html'

class StudentCreateView(LoginRequiredMixin, CreateView):
    form_class = StudentForm
    model = Student
    template_name = 'student_new.html'
    

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'student_edit.html'

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('students')

class StudentVerifyDetailView(DetailView):
    model = Student
    template_name = 'verify.html'