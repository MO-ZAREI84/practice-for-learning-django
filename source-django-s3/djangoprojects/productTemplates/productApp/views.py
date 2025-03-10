from django.shortcuts import render

def index(request):
    return render(request, "productApp/index.html")
    
def mobiles(request):
    mobiles = {
        'product1' : 'Nokia N95',
        'product2' : 'ios 13',
        'product3' : 'Shiaomi S2',
    }
    return render(request, "productApp/products.html" , context = mobiles)
    
def laptops(request):
    laptops = {
        'product1' : 'asus X1',
        'product2' : 'dell y12',
        'product3' : 'lenovo z12',
    }
    return render(request, "productApp/products.html" , context = laptops)
    
def gadgets(request):
    gadgets = {
        'product1' : 'gadget z1',
        'product2' : 'gadget z2',
        'product3' : 'gadget z3',
    }
    return render(request, "productApp/products.html" , context = gadgets)
