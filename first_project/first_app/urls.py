from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_age/<int:age>/', views.show_age, name='show_age'),
    path('forms/', views.forms, name='form')
]

