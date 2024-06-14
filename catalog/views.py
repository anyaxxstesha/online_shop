from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return render(request, 'index.html')
    return render(request, 'contacts.html')


def product_info(request, pk):
    """Контроллер, отвечающий за изображение отдельной страницы с товаром"""
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_info.html', context)
