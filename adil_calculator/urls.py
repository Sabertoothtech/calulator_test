from django.contrib import admin
from django.urls import path,include
from adil_calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculator, name='calculator'),
    path('result/', views.caculateresult, name='result')
]
