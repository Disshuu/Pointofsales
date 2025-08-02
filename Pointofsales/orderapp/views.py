from django.shortcuts import render, redirect
from orderapp.models import orderlist
from Digitalapp.models import Productlist
from Traditionalapp.models import Customerlist

def order_list_view(request):
    customers = Customerlist.objects.all()
    products = Productlist.objects.all()
    orders = orderlist.objects.all()

    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        address = request.POST.get('address') 

        orderlist.objects.create(
            customer_id=customer_id,
            product_id=product_id,
            quantity=quantity,
            address=address
        )
        return redirect('orderlist')

    return render(request, 'orderlist.html', {
        'customers': customers,
        'products': products,
        'orders': orders
    })
# orderapp/views.py

def edit_order(request, id):
    order = orderlist.objects.get(id=id)
    customers = Customerlist.objects.all()
    products = Productlist.objects.all()

    if request.method == 'POST':
        order.customer_id = request.POST.get('customer')
        order.product_id = request.POST.get('product')
        order.quantity = request.POST.get('quantity')
        order.address = request.POST.get('address')
        order.save()
        return redirect('orderlist')

    return render(request, 'edit_order.html', {
        'order': order,
        'customers': customers,
        'products': products
    })

def delete_order(request, id):
    order = orderlist.objects.get(id=id)
    order.delete()
    return redirect('orderlist')
    



