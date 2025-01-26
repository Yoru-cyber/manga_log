from django.db import models
from django.forms import ValidationError

# Create your models here.


class Item(models.Model):
    # Choices for the category field
    CATEGORY_CHOICES = [
        ("Manhwa", "Manhwa"),
        ("Manga", "Manga"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default="OTHER"
    )
    image = models.ImageField(
        upload_to="item_images/", null=True, blank=True
    )  # Images will be uploaded to 'media/item_images/'
    rating = models.IntegerField(
        help_text="Rating out of 10",  
    )  # Rating from 0 to 10
    review = models.TextField()

    def __str__(self):
        return self.name
