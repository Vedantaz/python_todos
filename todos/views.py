from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import ToDo
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return ToDo.objects.order_by('created_at')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'todos/register.html', {'form' : form})

def login(request):
    if request_method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid:
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'todos/login.html', {'form':form})
    
def logout(request):
    logout(request)
    return redirect('login')


def add(request):
    if(request.method == 'POST'):

        title = request.POST.get("title")
        if title:
            ToDo.objects.create(title=title, isCompleted=False)
        return redirect("todos:index")
    return render(request, "todos/index.html")

def delete(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)

    if request.method == 'POST':
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description", "")
        isCompleted = "isCompleted" in request.POST
        
        if isCompleted is not None:
            todo.isCompleted = isCompleted == 'on'
        
        todo.save()
        return redirect("todos:index") 
       
    return render(request, "todos/update.html", {"todo":todo})