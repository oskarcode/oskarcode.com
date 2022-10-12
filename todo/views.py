
# Create your views here.

from sqlite3 import IntegrityError
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def currenttodos(request):
          todos = Todo.objects.filter(user = request.user, datecompleted__isnull = True)
          return render(request, 'todo/currenttodos.html', {'todos':todos})


def home(request):
          return render(request, 'todo/home.html')


def createtodo(request):
          if request.method == 'GET':
                    return render(request, 'todo/createtodo.html', {'form': TodoForm()})
          else:
              try: 
                    form = TodoForm(request.POST)
                    newtodo = form.save(commit=False)
                    newtodo.user = request.user
                    newtodo.save()
                    return redirect('currenttodos')
              except ValueError:
                    return render(request, 'todo/createtodo.html', {'form': TodoForm(), 'error':'bad data passed in, try again'})


def viewtodo(request,todo_pk):
          todo = get_object_or_404( Todo, pk = todo_pk, user = request.user)
          if request.method == 'GET':
                    form = TodoForm(instance = todo)
                    return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
          else:
               try:
                    form = TodoForm(request.POST, instance=todo)
                    form.save()
                    return redirect('currenttodos')
               except ValueError:
                    return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error':'bad data passed in, try again'})


def completetodo(request, todo_pk):
          todo = get_object_or_404( Todo, pk = todo_pk, user = request.user)
          if request.method == 'POST':
                    todo.datecompleted = timezone.now()
                    todo.save()
                    return redirect('currenttodos')


def deletetodo(request, todo_pk):
          todo = get_object_or_404( Todo, pk = todo_pk, user = request.user)
          if request.method == 'POST':
                    todo.delete()
                    return redirect('currenttodos')

def completedtodos(request):
          todos = Todo.objects.filter(user = request.user, datecompleted__isnull = False).order_by('-datecompleted')
          return render(request, 'todo/completedtodos.html', {'todos':todos})


