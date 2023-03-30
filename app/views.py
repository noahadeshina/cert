from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, StudentForm, Certificate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from .cert_gen import make_certificates

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

def certificate(request, pk):
    obj = Student.objects.get(pk=pk)
    name = f'{obj.first_name} {obj.middle_name} {obj.last_name}'
    make_certificates(name)
    parent = 'cert_gen/cert_temp/'
    fn = name.replace(' ', '_').lower()
    file = f'{parent}/{fn}.png'
    certificate_obj = Certificate.objects.create(student=obj, certificate=file)
    certificate_obj.save()
    return HttpResponseRedirect(reverse('student_detail', args=[str(obj.id)]))

def view_cert(request, pk):
    obj = Certificate.objects.get(student=pk)
    context = {
        'cert' : obj,
    }
    return render(request, 'view_cert.html', context)