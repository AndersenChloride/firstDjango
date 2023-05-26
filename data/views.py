from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Drugs, Store
from .forms import StoreForm
from django.views.generic import DetailView, UpdateView


def data_home(request):
    data = Drugs.objects.order_by('name')
    return render(request, 'data/data_home.html', {'data': data})


def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            form.id_store = id
            form.save()
            return redirect('create_and_table')
    else:
        form = StoreForm()

    store = Store.objects.all()
    context = {
        'form': form,
        'store': store,
    }
    return render(request, 'data/create.html', context)


def table(request):
    store = Store.objects.all()
    return render(request, 'data/create.html', {'store': store})


