from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.

def index(request):
    if request.method == 'POST':
        productfield = Product(
            image = request.FILES.get('image'),
            title = request.POST['title'],
            price = request.POST['price']
        )
        productfield.save()
        return redirect ('shop')
    
    else:
        return render(request, 'index.html')
    

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('shop')


def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.title = request.POST['title']
        product.price = request.POST['price']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('shop')

    return render(request, 'update.html', {'product': product})