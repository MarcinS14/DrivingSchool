from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
#from drsch.forms import UserCreateForm
# Create your views here.

class SignUp (generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'
	
def home(request):

	return render(request, 'home.html')

def login(request):

	return render(request, 'login.html')

