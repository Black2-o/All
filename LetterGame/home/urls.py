from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homee"),
    path('start', views.start, name="start"),
    path('add', views.add, name="add"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('delete/<str:id>', views.delete, name="delete"),
]
