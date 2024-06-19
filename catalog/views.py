from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def goods(request):
    return render(request, 'goods.html')


def goods_list(request):
    good = Product.objects.all()
    context = {'product': good}
    return render(request, 'product_list.html', context)


def product(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    context = {'product': prod}
    return render(request, 'product.html', context)
