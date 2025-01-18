from django.http import HttpResponse
from django.shortcuts import render
from shop_side.models import Product, Category


def product_create_view(request):
    context = {'category_list': Category.objects.all()}

    if request.method == 'POST':

        name = request.POST.get('name')
        if not name:
            return HttpResponse('Name is required')
        price = request.POST.get('price')
        if not price:
            return HttpResponse('Price is required')
        quantity = request.POST.get('quantity')
        if not quantity:
            return HttpResponse('Quantity is required')
        category = request.POST.get('category')
        if not category:
            return HttpResponse('Category is required')

        product = Product()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(
            pk=category
        )

        product.save()

    return render(request,
                  'shop_side/product_create.html',
                  context)


