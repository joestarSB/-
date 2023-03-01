from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login
from .forms import LoginForm, UserRegistrationForm


User = get_user_model()

def signup(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password']
            )
            return redirect('login')
        return redirect('signup')
    return render(request, template_name='authapp/signup.html', context={
        'form': form
    })


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('login')
            return redirect('index')
    return render(request, 'authapp/login.html', context={
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('index')
