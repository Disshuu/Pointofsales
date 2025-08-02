# Traditionalapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from Traditionalapp.models import Customerlist

def customer_list_view(request):
    data = Customerlist.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        
        Customerlist.objects.create(name=name, email=email, contact=contact)
        return redirect('customerlist')

    return render(request, 'Customerlist.html', {'data': data})

def edit_customer(request, id):
    customer = get_object_or_404(Customerlist, id=id)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.contact = request.POST.get('contact')
        customer.save()
        return redirect('customerlist')

    return render(request, 'edit_customer.html', {'customer': customer})

def delete_customer(request, id):
    customer = get_object_or_404(Customerlist, id=id)
    customer.delete()
    return redirect('customerlist')

