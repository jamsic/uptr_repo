from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dir_menu_item/<int:menu_item_id>/',
         views.directories_menu_item, name='dir_menu_item'),
    path('res_menu_item/<int:menu_item_id>/',
         views.restaurant_menu_item, name='res_menu_item'),
]