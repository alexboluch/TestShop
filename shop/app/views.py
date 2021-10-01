from django.shortcuts import render
from .models import Item, Employee, Sale, NewPrice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from .forms import ItemBuyForm, RegistrForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from annoying.decorators import render_to
from django.contrib.auth.mixins import LoginRequiredMixin


@render_to('main.html')
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
    return context


class ItemBuyView(LoginRequiredMixin, CreateView):
    model = Sale
    template_name = 'item_detail.html'
    form_class = ItemBuyForm
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Item.objects.get(id=self.kwargs['pk'])
        context["item"] = item
        return context


    def form_valid(self, form):
        instance = form.save(commit=False)
        item = Item.objects.get(id=self.kwargs['pk'])
        instance.quantity = int(form.cleaned_data["quantity"])
        instance.final_price = item.price * instance.quantity
        instance.buyer = User.objects.get(username=self.request.user.username)
        instance.item = item
        instance.seller = item.seller
        instance.save()
        return redirect(self.success_url)


class Registration(CreateView):
    model = User
    template_name = 'registration/registration.html'
    form_class = RegistrForm
    success_url = '/'


@render_to('sales_history.html')
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
    return context


@render_to('new_prices.html')
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
    return context


