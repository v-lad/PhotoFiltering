from django.shortcuts import render, get_object_or_404, redirect


class FilterPageMixin:
    url = None

    def get(self, request):
        return render(request, self.url)
