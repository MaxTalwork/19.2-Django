from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import home, contacts, goods_list, product

app_name = NewappConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('goods/', goods_list, name='goods'),
    path('product/<int:pk>/', product, name='product')
]
