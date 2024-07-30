from django.urls import path
from .views import task_list, add_task, update_task, delete_task, upload_image

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('update/<int:pk>/', update_task, name='update_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('upload/', upload_image, name='upload_image'),
]
