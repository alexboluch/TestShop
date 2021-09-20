from django.shortcuts import render
from .models import Item, Employee, Sale
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


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

def item_detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
    'item':item,
    }
    return render(request, 'item_detail.html', context)



