from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from App.models import Product

class ProductListTemplateView(TemplateView):
    template_name = 'products_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class ProductsList(ListView):
    template_name = 'products_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', None)

        if sort_by == 'id':
            queryset = queryset.order_by('id')
        elif sort_by == 'price':
            queryset = queryset.order_by('price')
        else:
            queryset = queryset.order_by('product_name')

        return queryset

class ProductsDetail(DetailView):
    template_name = 'product_details.html'
    model = Product
    context_object_name = 'product'

class ProductsUpdate(UpdateView):
    template_name = 'product_update.html'
    model = Product
    fields = ['product_name', 'price', 'description', 'product_picture']

    def get_success_url(self):
        return reverse_lazy('product_details', kwargs={'pk': self.object.pk})

class ProductsDelete(DeleteView):
    template_name = 'product_delete.html'
    model = Product
    success_url = reverse_lazy('products_list')

class ProductsCreate(CreateView):
    template_name = 'product_create.html'
    model = Product
    fields = ['product_name', 'price', 'description', 'category', 'product_picture']
    success_url = reverse_lazy('products_list')
