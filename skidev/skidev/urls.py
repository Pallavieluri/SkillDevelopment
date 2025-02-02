"""
URL configuration for skidev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from course import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('profile/', views.profile_view, name='profile'),
#     path('logout/', views.logout_view, name='logout'),
#     path('course/', views.course_overview, name='course_overview'),
#     path('python-course/', views.python_course, name='python_course'),
#     path('web-development/', views.web_dev, name='web_dev'),
#     path('data-science/', views.data_science, name='data_science'),
#     path('cyber-security/', views.cyber_security, name='cyber_security'),
#     path('pyen/',views.pyen, name='pyen'),
#     path('web/',views.web, name='web'),
#     path('data/',views.data, name='data'),
#     path('cyber/',views.cyber, name='cyber')
# ]

from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from course import views  # Import your custom views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('course/', views.course_overview, name='course_overview'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),  

    path('python-course/', views.python_course, name='python_course'),
    path('web-development/', views.web_dev, name='web_dev'),
    path('data-science/', views.data_science, name='data_science'),
    path('cyber-security/', views.cyber_security, name='cyber_security'),
    path('pyen/',views.pyen, name='pyen'),
     path('web/',views.web, name='web'),
     path('data/',views.data, name='data'),
     path('cyber/',views.cyber, name='cyber')
]






