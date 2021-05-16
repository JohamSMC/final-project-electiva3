from django.urls import path

from subjects import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('finish_activity/<str:id_activity>', views.update_activity, name="finish_activity"),
]
