from django.shortcuts import render, redirect

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


def item_list(request):
    items = Item.objects.all()
    return render(request, "item_list.html", {"items": items})

def manga_items(request):
    # Filter items with category 'manga'
    manga_items = Item.objects.filter(category='MANGA')
    context = {
        'items': manga_items,
        'category': 'Manga',
    }
    return render(request, 'category_list.html', context)

def manhwa_items(request):
    # Filter items with category 'manhwa'
    manhwa_items = Item.objects.filter(category='MANHWA')
    context = {
        'items': manhwa_items,
        'category': 'Manhwa',
    }
    return render(request, 'category_list.html', context)
