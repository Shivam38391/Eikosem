
from django.urls import path
from . import views


urlpatterns = [
    path("list", views.TodoAV.as_view(), name="list" ),
]
