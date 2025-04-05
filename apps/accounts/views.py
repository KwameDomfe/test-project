from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):

    if request.method == 'POST':

        loginForm = AuthenticationForm (request, data=request.POST)
        
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect ('/')
    else:

        loginForm = AuthenticationForm (request)

    context = {
        'form' : loginForm
    }
    return render (
        request,
        'accounts/login.html',
        context
    )

def logout_view(request):
    
    if request.method == 'POST':
        logout(request)
        return redirect ('/accounts/login')
    
    return render (
        request,
        'accounts/logout.html',
        {}
    )

def register_view(request):

    registerForm = UserCreationForm(request.POST or None)

    if registerForm.is_valid():
        registerForm.save()
        return redirect ('/accounts/login')
    
    context = {
        'form': registerForm
    }
    return render (
        request,
        'accounts/register.html',
        context
    )