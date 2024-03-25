from django.urls import path
from . import views

urlpatterns = [
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),
]