from django.urls import path

from subjects import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add-subject', views.addsubject, name="add-subject")
]
