from django.urls import path
from django.contrib.auth import views as auth_views
from user import views as user_views

app_name = 'user'

urlpatterns = [
    # Login
    path('login', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='user-login'),
    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),
         name='user-logout'),
    # Cadastro
    path('register/', user_views.register, name='user-register'),
    # Perfil
    path('perfil/', user_views.profile, name='profile'),
    
    path('profile/update/', user_views.profile_update,
         name='user-profile-update'),    
]