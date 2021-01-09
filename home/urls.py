from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home , name='home'),
    path('services/',views.services, name='services'),
    path('skills/',views.skills, name='skills'),
    path('contact/',views.contact, name='contact'),
]
