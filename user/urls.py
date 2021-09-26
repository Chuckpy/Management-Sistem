from django.urls import path
from django.contrib.auth import views as auth_views
from user import views as user_views

app_name = 'user'

urlpatterns = [
    # Login
    path('login', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='login'),
    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),
         name='logout'),
    # Cadastro
    path('registro/', user_views.register, name='register'),
    # Perfil
    path('perfil/', user_views.profile, name='profile'),
    
    path('perfil/update/', user_views.profile_update,
         name='update'),    
    ]