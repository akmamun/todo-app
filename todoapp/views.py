from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import LoginForm

def index(request):
    todos = Todo.objects.all()
    context = {
    "todos":todos,
    }
    return render(request,"base.html",context)

@login_required
def add(request):
    if(request.method=='POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title,text=text)
        todo.save()
        return redirect('/todo')

    else:
        return render(request,"add.html")
@login_required
def details(request,id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo,
    }
    return render(request, "details.html", context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
        if user:
            return redirect("/todo")
        else:
            return HttpResponse("Login Failed Please enter correct!")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return HttpResponse("Your Already Todo Member")
            else:
                return HttpResponse("Error")

    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})