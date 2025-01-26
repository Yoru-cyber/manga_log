from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_item, name="add_item"),
    path("list/", views.item_list, name="item_list"),
        path('manga/', views.manga_items, name='manga_items'),
    path('manhwa/', views.manhwa_items, name='manhwa_items'),
]
