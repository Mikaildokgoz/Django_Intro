
from django.urls import path
from .views import home,abc

urlpatterns = [
    
    path('', home, name="home"),
    path('abc/',  abc, name="abc")
]
