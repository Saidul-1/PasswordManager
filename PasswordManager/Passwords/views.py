from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
def Signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if(password1 != password2):
            return render(request, 'signup.html', {'message' : 'Password did not matched'})

        duplicateUser = User.objects.filter(username = username)
        if(duplicateUser.exists()):
            return render(request, 'signup.html', {'message' : 'Username is already exists'})        
        
        user = User.objects.create(username = username, email = email)
        user.set_password(password1)
        user.save()
        messages.success(request, {'message' : 'Account Created Successfully!'})
        return redirect('/login/')
    return render(request, 'signup.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is None:
            return render(request, 'login.html', {'message' : 'Username or Password is Invalid'})
        else:

            login(request, user)
            return redirect('/home/')
    
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url = '/login/')
def Home(request):
    if request.method == 'POST':
        user = request.user
        platform = request.POST.get('platform')
        username = request.POST.get('username')
        password = request.POST.get('password')

        password_block = PasswordBlock(user = user, platform = platform, username = username, password = password)
        password_block.save()

        queryset_all = PasswordBlock.objects.filter(user = user)
        return render(request, 'index.html', context = {'PasswordBlocks': queryset_all})

    queryset_all = PasswordBlock.objects.filter(user = request.user)
    return render(request, 'index.html', context = {'user': request.user, 'PasswordBlocks': queryset_all})
        