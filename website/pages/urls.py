from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('Home',views.HomePage,name='Home'),
    path('dep',views.dep,name='dep'),
    path('login',views.login,name='login'),
    path('search',views.search,name='search'),
    
]