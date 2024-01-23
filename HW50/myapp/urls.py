from django.urls import path
from .views import TaskModelAPIView, UserCreateAPIView

urlpatterns = [
    path('task-endpoint/', TaskModelAPIView.as_view(), name='task-model-api'),
    path('', UserCreateAPIView.as_view(), name='create-user'),
]