from django.urls import path, include
from . import views
urlpatterns = [
    path("AllTasks/", views.TaskIndex),
    path("AddTasks/", views.CreateTask),
    path("EditTask/<int:id>/", views.UpdateTask),
    path("DeleteTask/<int:id>/", views.DeleteTask),
    path("CreateBox/", views.CreateBox)
]

