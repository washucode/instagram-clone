from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('', views.signup, name='signup'),
    path('home/', views.home, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'auth/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('profile/', views.profile , name = 'my_profile'),
    path('image/new', views.createimage.as_view(), name = 'post'),

]