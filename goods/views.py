from django.shortcuts import render

def catalog(request):
    return render(request, 'goods/catalog.html')


def ptoduct(request):
    return render(request, 'goods/product.html')