from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser





# Create your forms here.

class NewUserForm(forms.ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ("student_id", "email", "password")
		
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user