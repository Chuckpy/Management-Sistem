from django.urls import path

from .views import AboutPageView, HomePageView, ContactPageView

app_name = "pages"

urlpatterns = [
    path("sobre/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("contato",ContactPageView.as_view(), name="contact")
    
]