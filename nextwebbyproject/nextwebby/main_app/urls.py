from django.urls import path
from . import views

urlpatterns = [
    path('nextwebby/', views.nextwebby, name='nextwebby'),
    path('pythondev/', views.pythondev, name='pythondeveloper'),
    path('frontend/', views.frontend, name='frontenddeveloper'),
    path('dataanalyst/', views.dataanalyst, name='dataanalyst'),
]