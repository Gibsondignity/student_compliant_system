from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from .models import Complaint,Feedback
# from causes.models import Catagory


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content',]
        
        
# title
# details
# type
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('title', 'details', 'type')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}), 
            'details': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'type': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }