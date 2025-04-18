from django.urls import path
from .views import main, register, dashboard, user_logout
urlpatterns = [
    path('', main, name='main'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('user_logout/', user_logout, name='user-logout'),

]