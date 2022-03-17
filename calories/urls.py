
from django.urls import path
from .views import home_page,LoginPage,LogOutPage,select_food,register_user,ProfilePage,add_food,update_food,delete_food
urlpatterns = [
 path('', home_page,name='home'),
 path('login/',LoginPage,name='login'),
 path('logout/',LogOutPage,name='logout'),
 path('select_food/',select_food,name='select_food'),
 path('add_food/',add_food,name='add_food'),
 path('update_food/<str:pk>/',update_food,name='update_food'),
 path('delete_food/<str:pk>/',delete_food,name='delete_food'),
 path('register/',register_user,name='register'),
 path('profile/',ProfilePage,name='profile'),
]