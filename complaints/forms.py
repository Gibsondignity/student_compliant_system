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
        fields = ('title', 'details', 'department', 'type')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}), 
            'details': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'department': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'type': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }
        
        
class ComplaintFeedbackForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('title', 'details', 'type', 'status', 'comment')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'disabled':'True'}), 
            'details': forms.Textarea(attrs={'class': 'form-control', 'required': True, 'disabled':'True'}),
            'type': forms.Select(attrs={'class': 'form-control', 'required': True, 'disabled':'True'}),
            'status': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'comment': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }