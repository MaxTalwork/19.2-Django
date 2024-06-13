from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import home, contacts, goods_list

app_name = NewappConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts.html', contacts, name='contacts'),
    path('goods.html', goods_list, name='goods')
]
