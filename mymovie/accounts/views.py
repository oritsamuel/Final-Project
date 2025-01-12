from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout


#registration for new users
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        #check if form is valid
        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data.get('password1')

            #authenticate user
            user = authenticate(username=user.username, password=raw_password)

            #login user
            login(request, user)
            return redirect('myapi:home')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

#login for existing users
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('myapi:home')
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
            
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})

    return render(request, 'accounts/login.html')

#logout
def logout_user(request):
    logout(request)
    print('you are logged out')
    return redirect('accounts:login')