from django.urls import path
from .views import UserView
from .views import TaskView
from . import views

urlpatterns = [
    path('user/<int:pk>/', views.UserView.as_view(), name='user-list-create' ),
     path('task/<int:pk>/', views.TaskView.as_view(), name='task-list-create' ),
]
