from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(name, phone, message)
            return render(request, 'index.html')
        return render(request, self.template_name)

    def get(self, request):
        return render(request, self.template_name)
