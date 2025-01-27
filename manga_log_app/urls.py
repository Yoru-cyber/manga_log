from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_item, name="add_item"),
    path("list/", views.item_list, name="item_list"),
    path("update/<int:item_id>/", views.update_item, name="update_item"),
    path("delete/<int:item_id>/", views.delete_item, name="delete_item"),
    path("manga/", views.manga_items, name="manga_items"),
    path("manhwa/", views.manhwa_items, name="manhwa_items"),
    path("stats/", views.stats, name="stats"),
]
