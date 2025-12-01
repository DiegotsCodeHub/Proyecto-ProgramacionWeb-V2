from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .utils import send_verification_email

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib import messages

#Templates
def index(request):
    return render(request, "index.html", {})
def Web_view(request):
    return render(request, 'game.html',{})
def challenges_view(request):
    return render(request, 'challenges.html',{})
def resources_view(request):
    return render(request, 'resources.html',{})
def solutions_view(request):
    return render(request, 'solutions.html',{})
def profile_view(request):
    return render(request, 'profile.html',{})

#css
def baseStyle_view(request):
    return render(request, 'static/styles/baseStyle.css',{})
def layoutStyle_view(request):
    return render(request, 'static/styles/layout.css',{})
def resourcesStyle_view(request):
    return render(request, 'static/styles/resources.css',{})
def gameStyle_view(request):
    return render(request, 'static/styles/gameStyle.css',{})
def formsStyle_view(request):
    return render(request, 'static/styles/forms.css',{})


#Authentication Views
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Credenciales inválidas, revisa e intenta de nuevo.")
    return render(request, 'login.html',{})

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        emaildata = request.POST.get("email")

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'register.html',{})
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe. Por favor, elige otro.")
            return render(request, 'register.html',{})
        
        user = User.objects.create_user(username=username, email=emaildata, password=password1)
        user.is_active = False
        user.save()

        send_verification_email(request, user)

        messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
        return redirect("login")
    return render(request, 'register.html',{})

def verify_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Cuenta verificada exitosamente. Ahora puedes iniciar sesión.")
        return redirect("login")
    else:
        messages.error(request, "El enlace de verificación es inválido o ha expirado.")
        return redirect("register")