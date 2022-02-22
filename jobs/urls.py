from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('jobs/<int:job_id>', views.detail),
]
