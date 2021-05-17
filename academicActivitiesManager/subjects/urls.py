from django.urls import path

from subjects import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add-subject', views.addsubject, name="add-subject"),
    path('finish_activity/<str:id_activity>', views.update_activity, name="finish_activity"),
    path('notification_task/', views.notification_task, name="notification_task"),

]
