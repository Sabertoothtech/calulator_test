
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modulus_app/',views.homePageView),
    path('modulus_result/',views.calc_result),

]