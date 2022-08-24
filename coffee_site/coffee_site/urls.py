from django.contrib import admin
from django.urls import path
from django.urls import re_path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('order/', views.order, name="order"),
    path('aja/', views.aja, name='aja'),
]
