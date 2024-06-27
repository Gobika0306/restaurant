from django.shortcuts import render
from django.shortcuts import redirect
from .models import Order, MenuItem
from django.http import HttpResponse
from django.db.models import Sum
from django.db.models import F

def home(request):
    return render(request, 'home.html')

# def menu_view(request):
#     menu_items = MenuItem.objects.all()  # Query all menu items
#     return render(request, 'home.html', {'menu_items': menu_items})

def menu_view(request):
    starters = MenuItem.objects.filter(category='STARTERS')
    main_dishes = MenuItem.objects.filter(category='MAIN_DISHES')
    desserts = MenuItem.objects.filter(category='DESSERTS')
    drinks = MenuItem.objects.filter(category='DRINKS')

    context = {
        'starters': starters,
        'main_dishes': main_dishes,
        'desserts': desserts,
        'drinks': drinks,
    }
    return render(request, 'home.html', context)


def add_to_order(request):
    if request.method == 'POST':
        food_item_id = request.POST.get('food_item_id')
        quantity = request.POST.get('quantity')
        menu_item = MenuItem.objects.get(id=food_item_id)
        order = Order.objects.create(menu_item=menu_item, quantity=quantity)
        return redirect('menu')
    else:
        return redirect('menu') 
    


def order_summary(request):
    orders = Order.objects.select_related('menu_item').all()
    total_bill = sum(order.menu_item.price * order.quantity for order in orders)
    return render(request, 'menu.html', {'orders': orders, 'total_bill': total_bill})