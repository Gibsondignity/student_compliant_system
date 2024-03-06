from django.shortcuts import render

from users.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect, reverse

# Create your views here.
def admin_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect(reverse('home'))
                messages.error(request,"Sorry! You do not have an admin privileges. Login as a staff.")
                return render(request, 'administrator/login.html', context={"form":form})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    
        
    return render(request, 'administrator/login.html', context={"form":form})


