from django.urls import path
from .views import landing, CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path("", landing, name="landing"),          
    path("login/", CustomLoginView.as_view(), name="login"),     
    path("logout/", CustomLogoutView.as_view(), name="logout"),   
    path("register/", RegisterView.as_view(), name="register"), 
]
