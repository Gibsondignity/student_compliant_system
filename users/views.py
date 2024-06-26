from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import (
#     #UserRegisterForm,
#     # UserUpdateForm,
#     # ProfileUpdateForm
#     )

from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as an admin.")
				return redirect(reverse('home'))
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})




def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST or None)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("login")
		print(form.errors.as_data())
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"form":form})




def account_logout(request):
    logout(request)
    return redirect(reverse('login'))


