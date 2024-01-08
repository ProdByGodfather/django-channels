from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path("",views.panel,name="panel"),
    path('logout/',views.logout_view,name='logout'),
    # login auth user model
    path("login/", auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    # register have a view
    path('register/', views.RegisterView.as_view(), name='register'),
    path("profile/",views.Profile.as_view(),name='profile'),
    path("profile/<str:username>/",views.user_profile,name='user_profile')
]