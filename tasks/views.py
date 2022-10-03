from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Esta vista nos permite guardar datos de un usuario
def signup(request):
    # metodo get devolver a la pagina del formulario
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    # metodo POST hacemos validacion de datos y guardamos en la base de datos
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registramos usuarios con los modelos de django
            try:
                user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # usamos login para que nos guarde la sesion y nos cree cookies
                login(request, user)
                return redirect('tasks')

            except IntegrityError:
                 return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })    
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las contraseñas deben coincidir'
                }) 

def tasks(request):
    return render(request, 'tasks.html')

def signout(request):
    logout(request)
    return redirect('home')