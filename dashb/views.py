from django.shortcuts import render, redirect
from .models import Product, Category, hightech, laptop, sortieMat1
from .filters import CategoryFilter, RetourFilter, HightTechFilter, LaptopFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, HightechForm, PhoneForm, TabForm, LaptopForm, SortieMatForm
from django.db.models import Count, Sum, Aggregate


# Create your views here.

def search_laptop(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           laptops = laptop.objects.filter(num_serie__icontains=query)
           smat1= sortieMat1.objects.filter(retour__icontains=query)
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb/search_laptop.html', {'laptops': laptops,'prod':prod,'smat1':smat1})
       else:
           lap2 = laptop.objects.all()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()
           product = Product.objects.all()
           count_prod = product.count()
           count_lap = lap2.count()
           lap1 = laptop.objects.filter(brand__startswith="T14S GEN 1").annotate(num_brand=Count("brand"))
           lap01 = lap1.count()
           lap002 = laptop.objects.filter(brand__startswith="T450S").annotate(num_brand=Count("brand"))
           lap02 = lap002.count()
           lap3 = laptop.objects.filter(brand__startswith="T14S GEN 3").annotate(num_brand=Count("brand"))
           lap03 = lap3.count()
           lap4 = laptop.objects.filter(brand__startswith="81HN").annotate(num_brand=Count("brand"))
           lap04 = lap4.count()
           lap5 = laptop.objects.filter(brand__startswith="X1 EXTREME G5").annotate(num_brand=Count("brand"))
           lap05 = lap5.count()
           lap6 = laptop.objects.filter(brand__startswith="P16").annotate(num_brand=Count("brand"))
           lap06 = lap6.count()
           myFilter = LaptopFilter(request.GET, queryset=lap2)
           lap2 = myFilter.qs
           page = Paginator(lap2, 10)
           page_list = request.GET.get('page')
           page = page.get_page(page_list)
       context = {
               'page': page,
               'myFilter': myFilter,
               'count_prod': count_prod,
               'count_lap': count_lap,
               'phone': phone,
               'tablette': tablette,
               'lap01': lap01,
               'lap02': lap02,
               'lap03': lap03,
               'lap04': lap04,
               'lap05': lap05,
               'lap06': lap06
         }
       return render(request, 'dashb/laptop.html', context)
def search_phone(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           phones = hightech.objects.filter(imei__icontains=query)
           smat1= sortieMat1.objects.filter(retour__icontains=query)
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb/search_phone.html', {'phones': phones,'prod':prod,'smat1':smat1})
       else:
           high = hightech.objects.all()

           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO SPARK 8").annotate(num_marque=Count("marque"))
           phoneTS8 = phoneT.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO CAMON 16").annotate(num_marque=Count("marque"))
           phoneTC16 = phoneT.count()

           product = Product.objects.all()
           count_prod = product.count()
           lap2 = laptop.objects.all()
           count_lap = lap2.count()
           myFilter = HightTechFilter(request.GET, queryset=phone2)
           phone2 = myFilter.qs
           page = Paginator(phone2, 10)
           page_list = request.GET.get('page')
           page = page.get_page(page_list)
       context = {
               'page': page,
               'myFilter': myFilter,
               'count_prod': count_prod,
               'count_lap': count_lap,
               'phone': phone,
               'phoneTS8':phoneTS8,
               'phoneTC16':phoneTC16,
               'tablette': tablette
         }
       return render(request, 'dashb/phone.html', context)

def search_tab(request):
       if request.method == 'GET':
           query = request.GET.get('query')
           if query:
               tabs = hightech.objects.filter(imei__icontains=query)
               smat1 = sortieMat1.objects.filter(retour__icontains=query)
               prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
               return render(request, 'dashb/search_tab.html', {'tabs': tabs, 'prod': prod, 'smat1': smat1})
           else:
               high = hightech.objects.all()

               phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
               phone = phone2.count()
               tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
                   num_marque=Count("marque"))
               tablette = tablette2.count()
               product = Product.objects.all()
               count_prod = product.count()
               lap2 = laptop.objects.all()
               count_lap = lap2.count()
               tab1 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO P 701").annotate(
                   num_marque=Count("marque"))
               tab01 = tab1.count()
               tab2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO P 703").annotate(
                   num_marque=Count("marque"))
               tab02 = tab2.count()
               tab3 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO PP7E").annotate(
                   num_marque=Count("marque"))
               tab03 = tab3.count()

               myFilter = HightTechFilter(request.GET, queryset=tablette2)
               tablette2 = myFilter.qs
               page = Paginator(tablette2, 10)
               page_list = request.GET.get('page')
               page = page.get_page(page_list)
           context = {
               'page': page,
               'myFilter': myFilter,
               'count_prod': count_prod,
               'count_lap': count_lap,
               'phone': phone,
               'tablette': tablette,
               'tab01': tab01,
               'tab02': tab02,
               'tab03': tab03
           }
           return render(request, 'dashb/tab.html', context)


def search_sortie(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            smats = sortieMat1.objects.filter(designation__icontains=query)
            smat1 = sortieMat1.objects.filter(retour__icontains=query)
            prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
            return render(request, 'dashb/search_sortie.html', {'smats': smats, 'prod': prod, 'smat1': smat1})
        else:

            smat3 = sortieMat1.objects.all()

            phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
            phone = phone2.count()
            tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
                num_marque=Count("marque"))
            tablette = tablette2.count()
            product = Product.objects.all()
            count_prod = product.count()
            lap2 = laptop.objects.all()
            count_lap = lap2.count()

            myFilter = RetourFilter(request.GET, queryset=smat3)
            smat3 = myFilter.qs
            page = Paginator(smat3, 10)
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
        return render(request, 'dashb/sortie.html', context)

def search(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           products = Product.objects.filter(designation__icontains=query)
           smat1= sortieMat1.objects.filter(retour__icontains=query)
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb/search.html', {'products': products,'prod':prod,'smat1':smat1})
       else:
           product = Product.objects.all()
           count_prod = product.count()
           lap = laptop.objects.all()
           count_lap = lap.count()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
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
       return render(request, 'dashb/index.html', context)

def search_sport(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           products = Product.objects.filter(designation__icontains=query)
          # products = Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='SALLE SPORT'")
           smat1= sortieMat1.objects.filter(retour__icontains=query)
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb/search_sport.html', {'products': products,'prod':prod,'smat1':smat1})
       else:
          # product = Product.objects.all()
           product = Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='SALLE SPORT'")
           #count_prod = product.count()
           lap = laptop.objects.all()
           count_lap = lap.count()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()

          # myFilter = CategoryFilter(request.GET, queryset=sp)
          # sp = myFilter.qs
           page = Paginator(product, 10)
           page_list = request.GET.get('page')
           page = page.get_page(page_list)

       context = {
               'page': page,
              # 'myFilter': myFilter,
             #  'count_prod': count_prod,
               'count_lap': count_lap,
               'phone': phone,
               'tablette': tablette
         }
       return render(request, 'dashb/sport.html', context)

def index(request):
    product = Product.objects.all()
    #product=Product.objects.annotate(total_sum=Sum("quantity")).order_by("designation")
    product2 = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
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

@login_required
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



@login_required
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

@login_required
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

def phone_admin(request):
    phone3 = hightech.objects.all()

    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    product = Product.objects.all()
    count_prod = product.count()
    lap2 = laptop.objects.all()
    count_lap = lap2.count()

    page = Paginator(phone2, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-phone_admin')
    else:
        form = PhoneForm()

    context = {
        'page': page,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette':tablette
    }
    return render(request, 'dashb_admin/phone_add.html', context)
def phone_update(request, pk):
    item = hightech.objects.get(id=pk)
    if request.method=='POST':
        form = PhoneForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('dashb-phone_admin')
    else:
        form = PhoneForm(instance=item)
    context={
        'form': form,

    }
    return render(request, 'dashb_admin/phone_update.html', context)

def tab_admin(request):
    tab = hightech.objects.all()

    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    product = Product.objects.all()
    count_prod = product.count()
    lap2 = laptop.objects.all()
    count_lap = lap2.count()

    page = Paginator(tablette2, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = TabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-tab_admin')
    else:
        form = TabForm()

    context = {
        'page': page,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette':tablette
    }
    return render(request, 'dashb_admin/tab_add.html', context)

@login_required
def tab_update(request, pk):
    item = hightech.objects.get(id=pk)
    if request.method=='POST':
        form = TabForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('dashb-tab_admin')
    else:
        form = TabForm(instance=item)
    context={
        'form': form,

    }
    return render(request, 'dashb_admin/tab_update.html', context)
@login_required
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
@login_required
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

    phoneT = hightech.objects.filter(marque__startswith="TECHNO SPARK 8").annotate(num_marque=Count("marque"))
    phoneTS8 = phoneT.count()

    phoneT = hightech.objects.filter(marque__startswith="TECHNO CAMON 16").annotate(num_marque=Count("marque"))
    phoneTC16 = phoneT.count()


    product = Product.objects.all()
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    myFilter = HightTechFilter(request.GET, queryset=phone2)
    phone2= myFilter.qs
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
        'myFilter': myFilter,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'phoneTS8': phoneTS8,
        'phoneTC16': phoneTC16,
        'tablette':tablette
    }
    return render(request, 'dashb/phone.html', context)




def high_tech_tab(request):
    high = hightech.objects.all()

    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    tab1 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO P 701").annotate(num_marque=Count("marque"))
    tab01 = tab1.count()
    tab2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO P 703").annotate(num_marque=Count("marque"))
    tab02 = tab2.count()
    tab3 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO PP7E").annotate(num_marque=Count("marque"))
    tab03 = tab3.count()
    product = Product.objects.all()
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    myFilter = HightTechFilter(request.GET, queryset=tablette2 )
    tablette2 = myFilter.qs
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
        'myFilter': myFilter,
        'form': form,
        'count_prod': count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette':tablette,
        'tab01': tab01,
        'tab02': tab02,
        'tab03': tab03
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

    lap1 = laptop.objects.filter(brand__startswith="T14S GEN 1").annotate(num_brand=Count("brand"))
    lap01 = lap1.count()
    lap2 = laptop.objects.filter(brand__startswith="T450S").annotate(num_brand=Count("brand"))
    lap02 = lap2.count()
    lap3 = laptop.objects.filter(brand__startswith="T14S GEN 3").annotate(num_brand=Count("brand"))
    lap03 = lap3.count()
    lap4 = laptop.objects.filter(brand__startswith="81HN").annotate(num_brand=Count("brand"))
    lap04 = lap4.count()
    lap5 = laptop.objects.filter(brand__startswith="X1 EXTREME G5").annotate(num_brand=Count("brand"))
    lap05 = lap5.count()
    lap6 = laptop.objects.filter(brand__startswith="P16").annotate(num_brand=Count("brand"))
    lap06 = lap6.count()
    myFilter = LaptopFilter(request.GET, queryset=lap)
    lap = myFilter.qs
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
        'myFilter': myFilter,
        'form': form,
        'count_lap': count_lap,
        'count_prod': count_prod,
        'phone': phone,
        'lap01': lap01,
        'lap02': lap02,
        'lap03': lap03,
        'lap04': lap04,
        'lap05': lap05,
        'lap06': lap06,
        'tablette': tablette
    }
    return render(request, 'dashb/laptop.html', context)

def sport(request):
    product = Product.objects.all()
    sp= Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='SALLE SPORT'")
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()

   # myFilter = CategoryFilter(request.GET, queryset=product)
  #  product = myFilter.qs
    page = Paginator(sp, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
       # 'myFilter': myFilter,
        'count_prod':count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/sport.html', context)

def serveur(request):
    product = Product.objects.all()
    serveur= Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='SALLE SERVEUR'")
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()

   # myFilter = CategoryFilter(request.GET, queryset=product)
  #  product = myFilter.qs
    page = Paginator(serveur, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
        'count_prod':count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/serveur.html', context)
def transit(request):
    product = Product.objects.all()
    trans= Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='CENTRE TRANSIT'")
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()

   # myFilter = CategoryFilter(request.GET, queryset=product)
  #  product = myFilter.qs
    page = Paginator(trans, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
        'count_prod':count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/transit.html', context)

def kousseri(request):
    product = Product.objects.all()
    kous= Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='BUREAU KOUSSERI'")
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()

   # myFilter = CategoryFilter(request.GET, queryset=product)
  #  product = myFilter.qs
    page = Paginator(kous, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
        'count_prod':count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/kousseri.html', context)

def aird(request):
    product = Product.objects.all()
    aird= Product.objects.raw("SELECT * FROM dashb_product WHERE emplacement='BUREAU AIRD'")
    count_prod = product.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()

   # myFilter = CategoryFilter(request.GET, queryset=product)
  #  product = myFilter.qs
    page = Paginator(aird, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
        'count_prod':count_prod,
        'count_lap': count_lap,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/aird.html', context)

def sortieMat_index(request):
    smat = sortieMat1.objects.all()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    product = Product.objects.all()
    count_prod = product.count()
    myFilter = RetourFilter(request.GET, queryset=smat)
    smat = myFilter.qs
    page = Paginator(smat, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    if request.method == 'POST':
        form = SortieMatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-sortieMat_index')
    else:
        form = SortieMatForm()

    context = {
        'page': page,
        'myFilter': myFilter,
        'form': form,
        'count_lap': count_lap,
        'count_prod': count_prod,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb/sortie.html', context)
@login_required
def sortieMat_admin(request):
    smat = sortieMat1.objects.all()
    phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
    phone = phone2.count()
    tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(num_marque=Count("marque"))
    tablette = tablette2.count()
    lap = laptop.objects.all()
    count_lap = lap.count()
    product = Product.objects.all()
    count_prod = product.count()
    page = Paginator(smat, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = SortieMatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashb-sortieMat_admin')
    else:
        form = SortieMatForm()

    context = {
        'page': page,
        'form': form,
        'count_lap': count_lap,
        'count_prod': count_prod,
        'phone': phone,
        'tablette': tablette
    }
    return render(request, 'dashb_admin/sortieMat.html', context)

def sortieMat_update(request, pk):
    item = sortieMat1.objects.get(id=pk)
    if request.method == 'POST':
        form = SortieMatForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashb-sortieMat_admin')
    else:
        form = SortieMatForm(instance=item)

    context = {
        'form': form,

    }
    return render(request, 'dashb_admin/sortieMat_update.html', context)

def sortieMat_delete(request, pk):
    item = sortieMat1.objects.get(id=pk)
    if request.method == 'POST':
            item.delete()
            return redirect('dashb-sortieMat_admin')
    return render(request, 'dashb_admin/sortieMat_delete.html')

def index_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
            item.delete()
            return redirect('dashb-index_admin')
    return render(request, 'dashb_admin/index_delete.html')


def search_prodAd(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           products = Product.objects.filter(designation__icontains=query)
           smat1= sortieMat1.objects.filter(retour__icontains=query)
           form = ProductForm()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb_admin/index.html', {'products': products,
                                                             'prod':prod,'smat1':smat1,'form':form})

       else:
           product = Product.objects.all()
           form = ProductForm()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO SPARK 8").annotate(num_marque=Count("marque"))
           phoneTS8 = phoneT.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO CAMON 16").annotate(num_marque=Count("marque"))
           phoneTC16 = phoneT.count()
           count_prod = product.count()
           lap2 = laptop.objects.all()
           count_lap = lap2.count()
           myFilter = CategoryFilter(request.GET, queryset=product)
           product = myFilter.qs
           page = Paginator(product, 10)
           page_list = request.GET.get('page')
           page = page.get_page(page_list)

       context = {
               'page': page,
               'form': form,
               ' product ':product,
               'myFilter': myFilter,
               'count_prod': count_prod,
               'count_lap': count_lap,
               'phoneTS8':phoneTS8,
               'phoneTC16':phoneTC16,
         }
       return render(request, 'dashb_admin/index.html', context)

def search_phoneAd(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           phones = hightech.objects.filter(imei__icontains=query)
           smat1= sortieMat1.objects.filter(retour__icontains=query)

           form = PhoneForm()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb_admin/phone_add.html', {'phones': phones,
                                                                 'prod':prod,'smat1':smat1,'form':form})

       else:
           high = hightech.objects.all()
           form = PhoneForm()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO SPARK 8").annotate(num_marque=Count("marque"))
           phoneTS8 = phoneT.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO CAMON 16").annotate(num_marque=Count("marque"))
           phoneTC16 = phoneT.count()

           product = Product.objects.all()
           count_prod = product.count()
           lap2 = laptop.objects.all()
           count_lap = lap2.count()
           myFilter = HightTechFilter(request.GET, queryset=phone2)
           phone2 = myFilter.qs
           page = Paginator(phone2, 10)
           page_list = request.GET.get('page')
           page = page.get_page(page_list)
           form = PhoneForm()

       context = {
               'page': page,
               'form': form,
               'myFilter': myFilter,
               'count_prod': count_prod,
               'count_lap': count_lap,
               'phoneTS8':phoneTS8,
               'phoneTC16':phoneTC16,
               'tablette': tablette,
                'phone':phone,
                'count_prod':count_prod
         }
       return render(request, 'dashb_admin/phone_add.html', context)


def search_tabAd(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           tabs = hightech.objects.filter(imei__icontains=query)
           smat1= sortieMat1.objects.filter(retour__icontains=query)

           form = PhoneForm()
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb_admin/tab_add.html', {'tabs': tabs,'prod':prod,'smat1':smat1,'form':form})

       else:
           high = hightech.objects.all()
           form = TabForm()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO SPARK 8").annotate(num_marque=Count("marque"))
           phoneTS8 = phoneT.count()

           phoneT = hightech.objects.filter(marque__startswith="TECHNO CAMON 16").annotate(num_marque=Count("marque"))
           phoneTC16 = phoneT.count()

           product = Product.objects.all()
           count_prod = product.count()
           lap2 = laptop.objects.all()
           count_lap = lap2.count()
           myFilter = HightTechFilter(request.GET, queryset=tablette2)
           phone2 = myFilter.qs
           page = Paginator(tablette2, 10)
           page_list = request.GET.get('page')
           page = page.get_page(page_list)
           form = PhoneForm()

       context = {
               'page': page,
               'form': form,
               'myFilter': myFilter,
               'count_prod': count_prod,
               'count_lap': count_lap,
               'phoneTS8':phoneTS8,
               'phoneTC16':phoneTC16,
               'tablette': tablette,
                'phone': phone
         }
       return render(request, 'dashb_admin/tab_add.html', context)


def search_laptopAd(request):
   if request.method == 'GET':
       query = request.GET.get('query')
       if query:
           laptops = laptop.objects.filter(num_serie__icontains=query)
           smat1= sortieMat1.objects.filter(retour__icontains=query)
           form = LaptopForm()
           prod = Product.objects.values('designation').annotate(total_sum=Sum('quantity')).order_by('designation')
           return render(request, 'dashb_admin/laptop_add.html', {'laptops': laptops,'prod':prod,'smat1':smat1,'form':form})
       else:
           lap2 = laptop.objects.all()
           form = LaptopForm()
           phone2 = hightech.objects.filter(marque__startswith="TECHNO").annotate(num_marque=Count("marque"))
           phone = phone2.count()
           tablette2 = hightech.objects.filter(marque__startswith="TABLETTE TECHNO").annotate(
               num_marque=Count("marque"))
           tablette = tablette2.count()
           product = Product.objects.all()
           count_prod = product.count()

           count_lap = lap2.count()
           myFilter = LaptopFilter(request.GET, queryset=lap2)
           lap2 = myFilter.qs
           page = Paginator(lap2, 10)
           page_list = request.GET.get('page')
           page = page.get_page(page_list)
           form = LaptopForm()
       context = {
               'page': page,
               'myFilter': myFilter,
               'form': form,
               'count_prod': count_prod,
               'count_lap': count_lap,
               'phone': phone,
               'tablette': tablette
         }
       return render(request, 'dashb_admin/laptop_add.html', context)

