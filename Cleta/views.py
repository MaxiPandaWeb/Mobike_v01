from django.shortcuts import render
from Cleta.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo 

def registro(request):
    return render(request,'Cleta/registro.html')
def index(request):
    return render(request,'Cleta/index.html')
def pagos(request):
    return render(request,'Cleta/pagos.html')
def pago1(request):
    return render(request,'Cleta/pago1.html')
def pago2(request):
    return render(request,'Cleta/pago2.html')



@login_required
def special(request):
    return HttpResponse("Has iniciado sesión correctamente")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_perfil' in request.FILES:
                print('found it')
                profile.foto_perfil = request.FILES['foto_perfil']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'Cleta/registro.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Tu cuenta está inactiva")
        else:
            print("Alguien intentó iniciar sesión y falló")
            print("Usó el usuario: {} y contraseña: {}".format(username,password))
            return HttpResponse("Datos de ingreso incorrectos!")
    else:
        return render(request, 'Cleta/login.html', {})

def mostrar(request):
	userito = UserProfileInfo.objects.all()
	contexto = {'equisde':userito}
	return render(request, 'Cleta/index.html',contexto)



# Create your views here.
