from django.shortcuts import render,redirect
from products import items 
# Create your views here.
def index(request):
    if 'last_buy' in request.session.keys():
        del request.session['last_buy']
    context = {
        "items" : items
    }
    return render(request,'armadon_app/index.html',context)

def checkout(request):
    return render(request,'armadon_app/checkout.html')
    

def buy(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0
    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0
    
    request.session['total_charged']+= amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_buy'] = amount_charged
    
    return redirect('/checkout')

def go_back(request):
    return redirect('/')
