from django.urls import path

from AppTwo import views

urlpatterns = [
    path('', views.index, name='AppTwo-Home'),
    path('help/', views.user_help, name='Help'),
]
