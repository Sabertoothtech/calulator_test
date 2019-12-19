from django.contrib import admin
from django.urls import path
from multiply_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculator, name='calculator'),
    path('CalculateResult/', views.CalculateResult, name='CalculateResult'),
]
