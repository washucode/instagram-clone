from django.urls import include, path
from . import views

urlpatterns =[
    path('', views.login, name='login')
]