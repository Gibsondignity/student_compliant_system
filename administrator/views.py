from django.shortcuts import render

# Create your views here.
def admin_login(request):
    if request.method:
        
    return render(request, 'administrator/login.html')


