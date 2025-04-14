import os
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models.aggregates import Avg, Count

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
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = ItemForm(instance=item)
    return render(request, "update_item.html", {"form": form, "item": item})


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        root_path = os.getcwd()
        imgRemove = item.image.url
        os.remove(f'{root_path}/{imgRemove}')
        item.image = None
        item.delete()
        return redirect("item_list")  # Return empty response to remove the row
    return render(request, "partials/confirm_delete.html", {"item": item})


def item_list(request):
    items = Item.objects.all()  # Fetch all items
    paginator = Paginator(items, 10)  # Show 10 items per page
    page_number = request.GET.get("page")  # Get the current page number from the URL
    page_obj = paginator.get_page(
        page_number
    )  # Get the Page object for the current page
    return render(request, "category_list.html", {"page_obj": page_obj, "category": "General"})


def manga_items(request):
    # Filter items with category 'manga'
    manga_items = Item.objects.filter(category="Manga")
    paginator = Paginator(manga_items, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "category_list.html", {"page_obj": page_obj, "category": "Manga"}
    )


def manhwa_items(request):
    # Filter items with category 'manhwa'
    manhwa_items = Item.objects.filter(category="Manhwa")
    paginator = Paginator(manhwa_items, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "category_list.html", {"page_obj": page_obj, "category": "Manhwa"}
    )


def stats(request):
    count = Item.objects.all().count()
    count_manhwa = Item.objects.filter(category="Manhwa").count()
    count_manga = Item.objects.filter(category="Manga").count()
    avg_rating = Item.objects.aggregate(Avg("rating"))["rating__avg"]
    avg_rating_manhwa = Item.objects.filter(category="Manhwa").aggregate(Avg("rating"))[
        "rating__avg"
    ]
    avg_rating_manga = Item.objects.filter(category="Manga").aggregate(Avg("rating"))[
        "rating__avg"
    ]
    context = {
        "count": count,
        "count_manhwa": count_manhwa,
        "count_manga": count_manga,
        "avg_rating": avg_rating,
        "avg_rating_manhwa": avg_rating_manhwa,
        "avg_rating_manga": avg_rating_manga,
    }
    return render(request, "stats.html", context)
