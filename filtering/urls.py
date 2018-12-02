from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page_url"),
    path('filtering/', views.FilteringView.as_view(), name="filtering_url"),
    path('filtering/BnW', views.BnWFilterView.as_view(), name="BnW_filter_url"),
    path('filtering/Brightnes',
         views.BrightnesFilterView.as_view(), name="Brightnes_filter_url"),
    path('filtering/Grayscale',
         views.GrayscaleFilterView.as_view(), name="Grayscale_filter_url"),
    path('filtering/Negative', views.NegativeFilterView.as_view(),
         name="Negative_filter_url"),
    path('filtering/Noises', views.NoisesFilterView.as_view(),
         name="Noises_filter_url"),
    path('filtering/Sepia', views.SepiaFilterView.as_view(), name="Sepia_filter_url")
]
