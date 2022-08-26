from django.urls import path
from api.views import BlogListCreateAPI,BlogListViewUpdateDelete,SearchListCreateAPI

urlpatterns = [
    path('api/',BlogListCreateAPI.as_view()),
    path('api/<int:pk>/',BlogListViewUpdateDelete.as_view()),
    path('search/',SearchListCreateAPI.as_view()),
    ]
