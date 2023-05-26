from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('about', TemplateView.as_view(template_name="about.html"), name="about"),
    path('login', TemplateView.as_view(template_name="login.html"), name="login"),
    path('users/', include('users.urls')),

]
