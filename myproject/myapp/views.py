from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

def product_list(request):
    search=request.GET.get('search')
    if search:
        product_list=Product.objects.filter(name__icontains=search)
    else:
        product_liproduct_list = Product.objects.all().order_by("id")

    paginator=Paginator(product_list,5)  
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'search':search}) 

# Create your views here.
