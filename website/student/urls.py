from django.urls import path
from .import views

urlpatterns =[
    path('add',views.add,name='add'),
    path('StudentUpdate', views.StudentUpdate, name='student'),
    path('SerchUpdeta', views.SerchUpdate, name='students'),
    path('status',views.status,name='status'),
    path('<int:id>',views.Update,name='Update'),
    path('delete/<int:id>', views.Delete, name='delete'),

]