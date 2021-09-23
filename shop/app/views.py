from django.shortcuts import render
from .models import Item, Employee, Sale
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .forms import ItemBuyForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def main_view(request):
    items = Item.objects.all()
    paginator = Paginator(items, 5)
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


# def item_detail_view(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     context = {
#     'item':item,
#     }
#     return render(request, 'item_detail.html', context)


# def item_detail_view(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     context = {
#     'item':item,
#     }
#     return render(request, 'item_detail.html', context)


def item_buy_view(request, pk):
    data = {}
    item = get_object_or_404(Item, pk=pk)
    if request.POST:
        form = ItemBuyForm(request.POST)
        if form.is_valid():
            print("Valid")
            price = int(form.cleaned_data["price"])
            quantity = int(form.cleaned_data["quantity"])
            final_price = price * quantity
            user = User.objects.get(username="admin")
            self_item = Item.objects.get(title=form.cleaned_data["title"])
            self_seller = Employee.objects.get(name=form.cleaned_data["seller"])
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
    
    return render(request, 'item_detail.html', data)

