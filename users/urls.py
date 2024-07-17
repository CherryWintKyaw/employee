from django.urls import path
from .views import (
    user_list,
    user_create,
    user_detail,
    user_update,
    user_delete
)

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('users/<uuid:pk>/', user_detail, name='user_detail'),
    path('users/<uuid:pk>/update/', user_update, name='user_update'),
    path('users/<uuid:pk>/delete/', user_delete, name='user_delete'),
]
