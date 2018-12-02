from django.shortcuts import render
from django.views.generic import View
from .utills import FilterPageMixin


class HomeView(View):
    def get(self, request):
        return render(request, "filtering/home_page.html")


class FilteringView(View):
    def get(self, request):
        return render(request, "filtering/filtering.html")


class BnWFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/BnW_page.html"


class BrightnesFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/brightnes_page.html"


class GrayscaleFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/grayscale_page.html"


class NegativeFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/negative_page.html"


class NoisesFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/noises_page.html"


class SepiaFilterView(FilterPageMixin, View):
    url = "filtering/fil_pages/sepia_page.html"
