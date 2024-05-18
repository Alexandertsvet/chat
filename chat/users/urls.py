from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import SignUpView
from users.views import HomePage

app_name = 'users'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]