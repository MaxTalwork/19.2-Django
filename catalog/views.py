from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProdForm, VersionForm
from catalog.models import Product, Version


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def goods(request):
    return render(request, 'catalog/goods.html')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProdForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProdForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProdFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProdFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProdFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))




    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
