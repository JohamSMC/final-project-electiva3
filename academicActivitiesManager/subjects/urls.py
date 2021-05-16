from django.urls import path

from subjects import views

urlpatterns = [
    path('index/', views.index, name="index"),
]
