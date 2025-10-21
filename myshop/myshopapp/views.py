from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def my_product(request):
    if request.method == 'POST':
        myimage = Product(
            image = request.FILES.get('image'),
            title = request.POST['title'],
            price = request.POST['price']
        )
        myimage.save()
        return redirect ('shop')
    
    else:
        return render(request, 'index.html')