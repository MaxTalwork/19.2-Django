from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import goods_list, product, goods

app_name = NewappConfig.name
urlpatterns = [
    # path('', home, name='home'),
    # path('contacts.html', contacts, name='contacts'),
    path('', goods, name='goods'),
    path('product_list/', goods_list, name='product_list'),
    path('product/<int:pk>/', product, name='product')
]
