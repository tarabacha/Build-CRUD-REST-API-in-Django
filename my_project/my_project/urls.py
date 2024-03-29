"""my_project URL Configuration
hehehe
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:-
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
URL Updated
hahaha
"""
# from django.contrib import admin
from django.urls import path
from my_app.views import EmployeeDetails, ListEmployee

urlpatterns = [
#     path('admin/', admin.site.urls),
    ## Removed the admin site access in order stio data leaks
    path('employeedetails/', EmployeeDetails),
    path('listemployee/', ListEmployee.as_view()),
    path('updateemployee/<id>', UpdateEmployee.as_view())
]
