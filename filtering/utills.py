import os
from django.shortcuts import render, redirect
from PIL import ImageFilter, Image


class FilteringMixin:
    url = None
    form = None
    model = None

    def get(self, request):
        form = self.form()
        return render(request, self.url, context={'form': form})

    def post(self, request):

        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            link = request.POST["link"]
            instance = self.model(image=request.FILES["upload"])
            instance.save()

            return redirect(link)

        return render(request, self.url, context={"form": form})


class FilterPageMixin:
    url = None
    model = None
    filter_f = lambda a: None

    def get(self, request):

        obj = self.model.objects.last()

        img_url = obj.image.url
        img_path = obj.image.path
        obj.delete()
        im = Image.open(img_path)
        im1, name = self.filter_f(im)
        file_u, ext = os.path.splitext(img_url)
        file_p, ext = os.path.splitext(img_path)
        new_img_url = file_u + name + ".png"
        new_img_path = file_p + name + ".png"
        im1.save(new_img_path)

        return render(request, self.url, context={"url_image": new_img_url})
