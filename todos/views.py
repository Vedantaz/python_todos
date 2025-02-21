from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import ToDo
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch') # 🔒 restricting access by login compulsion
class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        # return ToDo.objects.order_by(user = self.request.user)
        return ToDo.objects.filter(user=self.request.user).order_by('created_at')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! You can now log in.")
            login(request, user)
            return redirect('todos:index')
        else:
            print("Form is invalid:", form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'todos/register.html', {'form' : form})

def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todos:index')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'todos/login.html', {'form':form})

def user_logout():
    logout(request, user)
    return redirect("todos:index")

@login_required
def add(request):
    if(request.method == 'POST'):

        title = request.POST.get("title")
        if title:
            ToDo.objects.create(title=title, isCompleted=False, user=request.user)
        return redirect("todos:index")
    return render(request, "todos/index.html")

@login_required
def delete(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id, user=request.user)
    todo.delete()

    return redirect('todos:index')

@login_required
def update(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id, user=request.user)

    if request.method == 'POST':
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description", "")
        isCompleted = "isCompleted" in request.POST
        
        if isCompleted is not None:
            todo.isCompleted = isCompleted == 'on'
        
        todo.save()
        return redirect("todos:index")  
       
    return render(request, "todos/update.html", {"todo":todo})