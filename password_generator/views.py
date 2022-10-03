
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
          return render(request, 'password_generator/home.html')


def password(request):
    characters = []
    thepassword = []
    number_chosen = 0
    if request.GET.get('lowercase'):
        lower = list('abcdefghijklmnopqrstuvwxyz')
        thepassword.extend(random.choices(lower,k=1))
        characters.extend(lower)  
        number_chosen += 1
    if request.GET.get('uppercase'):
        upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        characters.extend(upper)
        thepassword.extend(random.choices(upper,k=1))
        number_chosen += 1
    if request.GET.get('special'):
        special = list('!@#$%^&*()')
        characters.extend(special)
        thepassword.extend(random.choices(special,k=1))
        number_chosen += 1
    if request.GET.get('numbers'):
        number = list('0123456789')
        characters.extend(number)
        thepassword.extend(random.choices(number,k=1))
        number_chosen += 1
    length = int(request.GET.get('length') or 0)
  

    thepassword += random.choices(characters, k = length - number_chosen )
    

    return render(request, 'password_generator/password.html', {'password': thepassword})
