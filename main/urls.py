from django.urls import include, path,re_path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('', views.signup, name='signup'),
    path('home/', views.home, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'auth/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/thankyou.html'), name = 'logout'),
    path('profile/', views.profile , name = 'my_profile'),
    path('image/new', views.createimage.as_view(), name = 'post'),
    re_path(r'^comment/(?P<image_id>\d+)$',views.comments,name='comments'),
    re_path(r'^like/$',views.like_post,name='like_post'),
    re_path(r'^delete/(?P<image_id>\d+)$',views.delete,name='delete'),
    path('update/',views.update_profile,name='update_profile'),

]