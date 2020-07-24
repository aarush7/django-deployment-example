from django.urls import path,include
from first import views

app_name='first'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    path('login/',views.user_login,name='user_login'),
    
]

