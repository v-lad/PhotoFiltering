from django.shortcuts import render
from django.views.generic import View
from .utills import FilterPageMixin, FilteringMixin
from .forms import *
from .models import *


class HomeView(View):
    def get(self, request):
        return render(request, "filtering/home_page.html")


class FilteringView(FilteringMixin, View):
    url = "filtering/filtering.html"
    form = ImgSaveForm
    model = ImgSave


class BnWFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/BnW_page.html"
    model = ImgSave


class BrightnesFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/brightnes_page.html"
    model = ImgSave


class GrayscaleFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/grayscale_page.html"
    model = ImgSave


class NegativeFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/negative_page.html"
    model = ImgSave


class NoisesFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/noises_page.html"
    model = ImgSave


class SepiaFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/sepia_page.html"
    model = ImgSave
