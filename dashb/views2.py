from django.shortcuts import render, redirect
from .models import Product, Category, hightech, laptop
from .filters import CategoryFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, HightechForm, LaptopForm
from django.db.models import Count, Sum, Aggregate


# Create your views here.

def search(request):
   # if 'q' in request.GET:
   #     q = request.GET['q']
   #     prod = Product.objects.filter(designation__icontains=q)
   # else:
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           products = Product.objects.filter(designation__icontains=query)
           return render(request, 'dashb/index.html', {'products': products})
       else:
          products = Product.objects.all()
          context ={
              'products': products
          }
          return render(request, 'dashb/index.html', context)
def index(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            product = Product.objects.filter(designation__icontains=query)
            return render(request, 'dashb/index.html', {'product': product})
        else:
            product = Product.objects.all()
            count_prod = product.count()
            lap = laptop.objects.all()
            count_lap = lap.count()
            phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
            phone = phone2.count()
            tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
            tablette = tablette2.count()

            myFilter = CategoryFilter(request.GET, queryset=product)
            product = myFilter.qs

            page = Paginator(product, 10)
            page_list = request.GET.get('page')
            page = page.get_page(page_list)

            context = {
              'page': page,
              'myFilter': myFilter,
              'count_prod': count_prod,
              'count_lap': count_lap,
              'phone': phone,
              'tablette': tablette
             }
        return render(request,'dashb/index.html', context)


def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('dashb-index_admin')
    else:
        form = ProductForm(instance=item)
    context={
        'form': form,

    }
    return render(request, 'dashb_admin/product_update.html', context)


@login_required
def index_admin(request):
    product = Product.objects.all()
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()

    page = Paginator(product, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-index_admin')
    else:
        form = ProductForm()

    context = {
        'page': page,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette': tablette
    }
    return render(request,'dashb_admin/index.html', context)




def high_tech_admin(request):
    high = hightech.objects.all()

    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    product = Product.objects.all()
    count_prod = product.count()
    lap2 = laptop.objects.all()
    count_lap = lap2.count()

    page = Paginator(high, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = HightechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-high_tech_admin')
    else:
        form = HightechForm()

    context = {
        'page': page,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette':tablette
    }
    return render(request, 'dashb_admin/hightech_add.html', context)

def high_tech_update(request, pk):
    item = hightech.objects.get(id=pk)
    if request.method=='POST':
        form = HightechForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('dashb-high_tech_admin')
    else:
        form = HightechForm(instance=item)
    context={
        'form': form,

    }
    return render(request, 'dashb_admin/hightech_update.html', context)


def laptop_admin(request):
    lap = laptop.objects.all()
    count_lap= lap.count()
    product = Product.objects.all()
    count_prod = product.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    page = Paginator(lap, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-laptop_admin')
    else:
        form = LaptopForm()

    context = {
        'page': page,
        'form': form,
        'count_lap': count_lap,
        'count_prod': count_prod,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb_admin/laptop_add.html', context)
def laptop_update(request, pk):
    item = laptop.objects.get(id=pk)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashb-laptop_admin')
    else:
        form = LaptopForm(instance=item)

    context = {
        'form': form,

    }
    return render(request, 'dashb_admin/laptop_update.html', context)
def high_tech_phone(request):
    high = hightech.objects.all()

    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    product = Product.objects.all()
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()

    page = Paginator(phone2, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = HightechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-high_tech_phone')
    else:
        form = HightechForm()

    context = {
        'page': page,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette':tablette
    }
    return render(request, 'dashb/phone.html', context)

def high_tech_tab(request):
    high = hightech.objects.all()

    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    product = Product.objects.all()
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()

    page = Paginator(tablette2, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = HightechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-high_tech_tab')
    else:
        form = HightechForm()

    context = {
        'page': page,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette':tablette
    }
    return render(request, 'dashb/tab.html', context)

def laptop_index(request):
    lap = laptop.objects.all()
    count_lap= lap.count()
    product = Product.objects.all()
    count_prod = product.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    page = Paginator(lap, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-laptop_index')
    else:
        form = LaptopForm()

    context = {
        'page': page,
        'form': form,
        'count_lap': count_lap,
        'count_prod': count_prod,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/laptop.html', context)

def sport(request):
    sp= Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='SALLE SPORT'")
    lap = laptop.objects.all()
    count_lap = lap.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()


    page = Paginator(sp, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
        'count_lap': count_lap,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/index.html', context)


