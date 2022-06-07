from django.urls import path

from authapp.views import login, logout

app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
