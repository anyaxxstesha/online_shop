from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_products_from_cache, get_categories_from_cache


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in self.object_list:
            product.active_version = product.versions.filter(is_current_version=True).first()
        return context

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:index")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.author = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("catalog:product_info", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author:
            return ProductForm
        if user.has_perm("catalog.can_cancel_publication") and user.has_perm(
                "catalog.can_edit_description") and user.has_perm("catalog.can_change_category"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:index")


class ContactsView(View):
    template_name = 'contacts.html'

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


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_categories_from_cache()
