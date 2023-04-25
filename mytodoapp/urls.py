
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("todo", views.TodoAV.as_view(), name="todo" ),
     path('todo/<int:pk>/', views.TodoAV.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)