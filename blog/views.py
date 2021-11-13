from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.


def index(request):
    category = Category.objects.all()
    if request.method == "POST":
        print(request.POST)
        category = Category.objects.get(name=request.POST['category'])
        product = Products.objects.create(
            category=category,
            name=request.POST['name'],
            price=request.POST['price'],
            amount=request.POST['amount'],
            desc=request.POST['desc']
        )
        product.save()
        return redirect('/blog')
    return render(request, 'forms.html', {'category': category})


def home(request):
    client = Products.objects.all()
    return render(request, 'home.html', {'products': client})


def home1(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'home1.html', context)


def edit(request, id):
    product = Products.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.amount = request.POST['amount']
        product.desc = request.POST['desc']
        product.save()
        return redirect('/blog')
    return render(request, 'edit_form.html', {'products': product})


def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('/blog')



