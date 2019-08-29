import os
from django.shortcuts import render, redirect
from PIL import ImageFilter, Image
import base64
from io import BytesIO
from time import monotonic

class FilteringMixin:
    url = None
    form = None
    model = None

    def get(self, request):
        form = self.form()
        return render(request, self.url, context={'form': form})

    def post(self, request):
        
        print()
        print(request.POST)
        print()
        print(request.FILES)
        print()

        form = self.form(request.POST, request.FILES)
        if request.FILES:
            link = request.POST["link"]
            instance = self.model(image=request.FILES["upload"])
            instance.save()

            return redirect(link)
        else:
            new_form = self.form()
            return render(request, self.url, context={'form': form, "new_f": new_form})

        return render(request, self.url, context={"form": form, "err_msg": True})


class FilterPageMixin:
    url = None
    model = None
    filter_f = lambda a: None

    def get(self, request):

        obj = self.model.objects.last()

        img_url = obj.image.url
        img_path = obj.image.path
        
        im = Image.open(img_path)
        im1, name = self.filter_f(im)
        # file_u, ext = os.path.splitext(img_url)
        # file_p, ext = os.path.splitext(img_path)
        # new_img_url = file_u + name + ".png"
        # new_img_path = file_p + name + ".png"
        obj.delete()
        
        buffer = BytesIO()
        im1.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())

        return render(request, self.url, context={
            # "url_image": new_img_url,
            'img_str': str(img_str)[2:-1],
        })
