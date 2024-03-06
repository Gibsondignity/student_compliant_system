"""Complain_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from complaints import views
from administrator import views as admin_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('home/', views.dashboard,name='home'),
    path("", user_views.login_request, name="login"),
    path('logout/',user_views.account_logout,name='logout'),
    
    
    path('make_complain/', views.make_complain,name='make_complain'),
    path('solved_compliants/', views.solved_compliants ,name='solved_compliants'),
    path('unsolved_compliants/', views.unsolved_compliants ,name='unsolved_compliants'),
    path('viewCompliant/', views.viewCompliant ,name='viewCompliant'),
    path('update_compliant/', views.update_compliant ,name='update_compliant'),
    path('delete_compliant/', views.delete_compliant ,name='delete_compliant'),
    
    
    path('admin_dashboard/', admin_views.admin_dashboard ,name='admin_dashboard'),
    path('admin_solved_compliants/', admin_views.admin_solved_compliants ,name='admin_solved_compliants'),
    path('admin_unsolved_compliants/', admin_views.admin_unsolved_compliants ,name='admin_unsolved_compliants'),
    path('all_complaints/', admin_views.all_complaints ,name='all_complaints'),
    path('admin_update_compliant/', admin_views.update_compliant ,name='admin_update_compliant'),
    path('admin_delete_compliant/', admin_views.delete_compliant ,name='admin_delete_compliant'),
    
    
    path('notifications/', admin_views.view_notifications, name='view_notifications'),
    path('in-progress/', admin_views.inProgress, name='inprogress'),
    
    path('administrator/login', admin_views.admin_login ,name='admin_login'),
    
    
    
]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)