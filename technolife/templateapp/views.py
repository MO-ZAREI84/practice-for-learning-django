from django.shortcuts import render

def index(request):
    product = {
        'product1':'mobile',
        'product2':'laptop',
        'product3':'gadgets',
    }
    return render(request,'templateapp/index.html',product)

def mobiles(request):
    product = {
        'product1':'nokia 121',
        'product2':'nokia 121',
        'product3':'nokia 121',
    }

    return render(request,'templateapp/product.html',product)
def laptops(request):
    product = {
        'product1':'asuz',
        'product2':'lenovo',
        'product3':'ios',
    }

    return render(request,'templateapp/product.html',product)

def gadgets(request):
    product = {
        'product1':'gadjet z1',
        'product2':'gadjet zq',
        'product3':'gadjet z3',
    }

    return render(request,'templateapp/product.html',product)