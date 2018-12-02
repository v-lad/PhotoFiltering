from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page_url"),
    path('filtering/', views.FilteringView.as_view(), name="filtering_url")
]
