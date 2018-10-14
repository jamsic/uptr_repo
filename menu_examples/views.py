from django.shortcuts import render
from menu.models import Menu


def index(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus,
    }
    return render(request, 'menu_examples/index.html', context)

def directories_menu_item(request, menu_item_id):
    context = {
        'menu_item_id': menu_item_id,
    }
    return render(request, 'menu_examples/dir_menu_item.html', context)

def restaurant_menu_item(request, menu_item_id):
    context = {
        'menu_item_id': menu_item_id,
    }
    return render(request, 'menu_examples/res_menu_item.html', context)
