from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy
class home(TemplateView):
    template_name ='app/home.html'


class schoollist(ListView):
    model=School
    context_object_name='school'
    

class Schooldetail(DetailView):
    model=School
    context_object_name='detail'


class School_Create(CreateView):
    model=School
    fields='__all__'



class School_update(UpdateView):
    model=School
    fields='__all__'


class Schooldelete(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('schoollist')