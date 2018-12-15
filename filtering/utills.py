from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect


class FilteringMixin:
    url = None
    form = None
    model = None

    def get(self, request):
        form = self.form()
        return render(request, self.url, context={'form': form})

    def post(self, request):
        
        # instance = get_object_or_404(self.model, id)
        form = self.form(request.POST, request.FILES)
        # print()
        # print(form)
        # print()
        if form.is_valid():

            # print()
            # print(request.POST)
            # print()
            link = request.POST["link"]
            
            instance = self.model(image=request.FILES["upload"])
            instance.save()

            return redirect(link)

        return render(request, self.url, context={"form": form})


class FilterPageMixin:
    url = None
    model = None

    def get(self, request):
        obj = self.model.objects.last()
        # print()
        # print(type(obj.image.url))
        # print(obj.image.path)
        # print()
        return render(
            request, self.url, context={self.model.__name__.lower(): obj})
