from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/main.html')

def products(request):
    return render(request, 'mainapp/products')

def contacts(request):
    return render(request, 'mainapp/contacts')

# Create your views here.
