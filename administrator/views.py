from django.shortcuts import render

# Create your views here.
def admin_login(request):
    if request.method:
        print("Request has gone through")
    return render(request, 'administrator/login.html')


