from django.contrib import admin
from django.urls import path
from abhical import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition', views.calculator, name='calculator'),
    path('CalculateResult/', views.CalculateResult, name='CalculateResult'),
]

