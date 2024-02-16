from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
# Create your views here.


class SchoolList(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'
    

