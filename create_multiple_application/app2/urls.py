from django.urls import path,include
from . import views

urlpatterns = [
    path("np/",views.next_page,name='np')
]
