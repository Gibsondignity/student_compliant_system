from django.contrib import admin
from .models import Staff, CustomUser

admin.site.register(CustomUser)
admin.site.register(Staff)
