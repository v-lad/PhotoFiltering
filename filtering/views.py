from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, "filtering/home_page.html")


class FilteringView(View):
    def get(self, request):
        return render(request, "filtering/filtering.html")
