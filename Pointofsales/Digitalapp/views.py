
# Create your views here.
from django.shortcuts import render, redirect
from Digitalapp.models import Productlist

# Create your views here.
def product_list_view(request):
    data= Productlist.objects.all() # getting all the data from the table to django
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        discount = request.POST.get('discount')
        
        
        Productlist_instances = Productlist(name=name,price=price,quantity=quantity,discount=discount)
        Productlist_instances.save()
        
        return redirect('productlist')
    return render(request, 'Productlist.html',{'data':data})
    #return HttpResponse("Hello, This is the new home page")
    
def edit(request,id):
    data= Productlist.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        discount = request.POST.get('discount')
        
        data.name = name
        data.price = price
        data.quantity = quantity
        data.discount=discount
        data.save()
        
       
        return redirect('productlist')
    return render(request, 'edit.html',{'data':data})
    

def delete(request,id):
    data = Productlist.objects.get(id=id)
    data.delete()
    return redirect('productlist')
    
