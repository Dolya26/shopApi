from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreatedOrderView.as_view()),
]
