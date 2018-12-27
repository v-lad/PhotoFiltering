import os
from django.shortcuts import render
from django.views.generic import View
from PIL import ImageFilter, Image, ImageDraw
from .utills import FilterPageMixin, FilteringMixin
from .forms import ImgSaveForm
from .models import ImgSave


class HomeView(View):
    def get(self, request):
        return render(request, "filtering/home_page.html")


class FilteringView(FilteringMixin, View):
    url = "filtering/filtering.html"
    form = ImgSaveForm
    model = ImgSave


class BnWFilterView(FilterPageMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "filtering/fil_pages/BnW_page.html"
        self.model = ImgSave
        self.filter_f = self.filtering

    @staticmethod
    def filtering(img):

        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]
        pix = img.load()
        factor = 30

        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = a + b + c
                if (S > (((255 + factor) // 2) * 3)):
                    a, b, c = 255, 255, 255
                else:
                    a, b, c = 0, 0, 0
                draw.point((i, j), (a, b, c))

        return (img, "BnW")


class BrightnesFilterView(FilterPageMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "filtering/fil_pages/brightnes_page.html"
        self.model = ImgSave
        self.filter_f = self.filtering

    @staticmethod
    def filtering(img):

        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]
        pix = img.load()
        factor = 80

        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + factor
                b = pix[i, j][1] + factor
                c = pix[i, j][2] + factor
                if a < 0:
                    a = 0
                if b < 0:
                    b = 0
                if c < 0:
                    c = 0
                if a > 255:
                    a = 255
                if b > 255:
                    b = 255
                if c > 255:
                    c = 255
                draw.point((i, j), (a, b, c))

        return (img, "BRIGHT")


class GrayscaleFilterView(FilterPageMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "filtering/fil_pages/grayscale_page.html"
        self.model = ImgSave
        self.filter_f = self.filtering

    @staticmethod
    def filtering(img):

        im1 = img.convert("L")

        return (im1, "GRAY")


class NegativeFilterView(FilterPageMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "filtering/fil_pages/negative_page.html"
        self.model = ImgSave
        self.filter_f = self.filtering

    @staticmethod
    def filtering(img):

        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]
        pix = img.load()

        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                draw.point((i, j), (255 - a, 255 - b, 255 - c))

        return (img, "NEG")


class NoisesFilterView(FilterPageMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "filtering/fil_pages/noises_page.html"
        self.model = ImgSave
        self.filter_f = self.filtering

    @staticmethod
    def filtering(img):
        from random import randint

        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]
        pix = img.load()
        factor = 70
        for i in range(width):
            for j in range(height):
                rand = randint(-factor, factor)
                a = pix[i, j][0] + rand
                b = pix[i, j][1] + rand
                c = pix[i, j][2] + rand
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))

        return (img, "NOISE")


class SepiaFilterView(FilterPageMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "filtering/fil_pages/sepia_page.html"
        self.model = ImgSave
        self.filter_f = self.filtering

    @staticmethod
    def filtering(img):

        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]
        pix = img.load()
        depth = 40

        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                a = S + depth * 2
                b = S + depth
                c = S
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))

        return (img, "SEPIA")


class BlurFilterView(FilterPageMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "filtering/fil_pages/blur_page.html"
        self.model = ImgSave
        self.filter_f = self.filtering

    @staticmethod
    def filtering(img):

        im1 = img.filter(ImageFilter.BoxBlur(4))

        return (im1, "BLUR")
