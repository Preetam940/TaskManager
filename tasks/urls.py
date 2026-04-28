from django.urls import path
from tasks.views import dashboard,add_task,user_login,register,user_logout
urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('add_task/',add_task,name='add_task'),
    path('login/',user_login,name='login'),
    path('register/',register,name='register'),
    path('logout/',user_logout,name='logout')
]
