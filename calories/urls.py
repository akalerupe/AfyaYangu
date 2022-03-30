
from .views import index,delete_consume,register_user
from django.urls import path
urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:id>/', delete_consume, name="delete"),
    path('register/',register_user,name='register')
]

