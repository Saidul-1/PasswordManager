from django.urls import path
from .views import *

urlpatterns = [
    path('', Redirect, name = 'redirect_to_home'),
    path('signup/', Signup, name = 'signup'),
    path('login/', Login, name = 'login'),
    path('logout/', Logout, name = 'logout'),
    path('home/', Home, name = 'home'),
]