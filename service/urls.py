"""
URL configuration for gasservice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', views.submit, name='submit'),
    path('info/',views.account_info,name='info'),
    path('status/',views.status,name='status'),
    path('login',views.login_user,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_info',views.user_info,name='userinfo'), 
    path('customer-detail',views.customer_details,name='cutomer_details'),
    path('delete/<int:id>', views.delete_record, name='delete_record'),
    path('edit/<int:id>/', views.edit_record, name = 'edit_record'),
   

    
]