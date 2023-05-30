from django.shortcuts import render, HttpResponse
from .models import Product


def product_list_view(request):
    context = {
        "text": "Hello",
        "products": Product.objects.all()
    }

    return render(request, "index.html", context)



def product_detail_view(request, id):
    context = {
        "id": id,
        "products": Product.objects.all()
    }

    return render(request, "detail.html", context)