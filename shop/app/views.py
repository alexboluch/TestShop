from django.shortcuts import render
from .models import Item, Employee, Sale, NewPrice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .forms import ItemBuyForm, RegistrForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def main_view(request):
    items = Item.objects.all()
    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        posts = paginator.page(1)  
    except EmptyPage:   
        posts = paginator.page(paginator.num_pages)
    context = {
        'items':posts,
        'page': page,
    }
    return render(request, 'main.html', context)


# @login_required(login_url='/accounts/login/')
# def item_buy_view(request, pk):
#     data = {}
#     item = get_object_or_404(Item, pk=pk)
#     if request.POST:
#         form = ItemBuyForm(request.POST)
#         if form.is_valid():
#             print("Valid")
#             price = int(form.cleaned_data["price"])
#             quantity = int(form.cleaned_data["quantity"])
#             final_price = price * quantity
#             user = User.objects.get(username=request.user.username)
#             self_item = Item.objects.get(title=form.cleaned_data["title"])
#             self_seller = Employee.objects.get(name=form.cleaned_data["seller"])
#             new_sale = Sale(
#                 final_price=final_price,
#                 quantity=quantity,
#                 item=self_item,
#                 seller=self_seller,
#                 buyer=user
#                 )
#             new_sale.save()
#             return HttpResponseRedirect("/")
#         else:
#             print("NOT Valid")
#             data['form'] = form
#             return render(request, 'item_detail.html', data)
#     else:
#         form = ItemBuyForm(instance=item)
#         data['form'] = form
    
#     return render(request, 'item_detail.html', data)

@login_required(login_url='/accounts/login/')
def item_buy_view(request, pk):
    data = {}
    item = get_object_or_404(Item, pk=pk)
    if request.POST:
        form = ItemBuyForm(request.POST)
        if form.is_valid():
            print("Valid")
            price = item.price
            quantity = int(form.cleaned_data["quantity"])
            final_price = price * quantity
            user = User.objects.get(username=request.user.username)
            self_item = item
            self_seller = item.seller
            new_sale = Sale(
                final_price=final_price,
                quantity=quantity,
                item=self_item,
                seller=self_seller,
                buyer=user
                )
            new_sale.save()
            return HttpResponseRedirect("/")
        else:
            print("NOT Valid")
            data['form'] = form
            return render(request, 'item_detail.html', data)
    else:
        form = ItemBuyForm(instance=item)
        data['form'] = form
        data['item'] = item
    
    return render(request, 'item_detail.html', data)


def registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    data = {}
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            print("valid")
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/')
        else:
            print("not valid")
            data['form'] = form
            return render(request, 'registration/registration.html', data)
    else:
        form = RegistrForm()
        data['form'] = form
        return render(request, 'registration/registration.html', data)


@login_required(login_url='/accounts/login/')
def sales_history_view(request):
    sales = Sale.objects.all()
    paginator = Paginator(sales, 10)
    page = request.GET.get('page')
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        posts = paginator.page(1)  
    except EmptyPage:   
        posts = paginator.page(paginator.num_pages)
    context = {
        'sales':posts,
        'page': page,
    }
    return render(request, 'sales_history.html', context)


@login_required(login_url='/accounts/login/')
def prices_history_view(request):
    prices = NewPrice.objects.all()
    paginator = Paginator(prices, 10)
    page = request.GET.get('page')
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        posts = paginator.page(1)  
    except EmptyPage:   
        posts = paginator.page(paginator.num_pages)
    context = {
        'prices':posts,
        'page': page,
    }
    return render(request, 'new_prices.html', context)


