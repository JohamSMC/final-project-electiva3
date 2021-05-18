from django.urls import path

from subjects import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add-subject', views.addsubject, name="add-subject"),
    path('finish_activity/<str:id_activity>', views.update_activity, name="finish_activity"),
    path('add_activity', views.add_activity, name="add-activity"),
    path('notification_task/', views.notification_task, name="notification_task"),
    path('delete_subject/<str:id_subject>', views.delete_subject, name="delete-subject"),
    path('delete_activity/<str:id_activity>', views.delete_activity, name="delete-activity"),
]
