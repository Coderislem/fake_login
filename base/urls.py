from django.urls import path
from base import views
urlpatterns = [
    path('login/',views.login,name='login')
]
