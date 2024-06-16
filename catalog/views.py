from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def goods_list(request):
    goods = Product.objects.all()
    context = {'product': goods}
    return render(request, 'goods.html', context)
