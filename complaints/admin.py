from django.contrib import admin
from .models import Complaint,Feedback
# Register your models here.

class CompliantAdmin(admin.ModelAdmin):
    list_display = ["title", 'details', 'type', 'user', 'status', 'comment', 'date_posted']
    
    
admin.site.register(Complaint, CompliantAdmin)
admin.site.register(Feedback)