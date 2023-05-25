from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),

    path('home1', views.home1, name='home1'),

    path('contact', views.contact, name='contact'),

    path('product', views.product, name='product'),

    path('choco', views.choco, name='choco'),

    path('gdgts', views.gdgts, name='gdgts'),

    path('bgs', views.bgs, name='bgs'),

    path('about', views.about, name='about'),

    path('login', views.login, name='login'),

    path('register', views.register, name='register'),

    path('logout', views.logout, name='logout')
]
