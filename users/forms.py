from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser





# Create your forms here.

class NewUserForm(forms.ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ("student_id", "first_name", "last_name", "email", "password", "confirm_password")
		
	widgets = {
		'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
		'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
	}
 
	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user