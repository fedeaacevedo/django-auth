from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html')


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
                return HttpResponse('Usuario creado exitosamente')

            except:
                return HttpResponse('El usuario ya existe')
        return HttpResponse('Contraseñas no coinciden')
