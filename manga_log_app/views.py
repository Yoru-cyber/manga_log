from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from .forms import ItemForm
from .models import Item


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = ItemForm()
    return render(request, "add_item.html", {"form": form})

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = ItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect("item_list")  # Return empty response to remove the row
    return render(request, 'partials/confirm_delete.html', {'item': item})

def item_list(request):
    items = Item.objects.all()
    return render(request, "item_list.html", {"items": items})


def manga_items(request):
    # Filter items with category 'manga'
    manga_items = Item.objects.filter(category="Manga")
    context = {
        "items": manga_items,
        "category": "Manga",
    }
    return render(request, "category_list.html", context)


def manhwa_items(request):
    # Filter items with category 'manhwa'
    manhwa_items = Item.objects.filter(category="Manhwa")
    context = {
        "items": manhwa_items,
        "category": "Manhwa",
    }
    return render(request, "category_list.html", context)
