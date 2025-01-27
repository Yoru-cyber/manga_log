from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "category", "image", "rating", "review"]
        labels = {
            "name": "Nombre",
            "category": "Categoría",
            "image": "Imagen",
            "rating": "Calificación",
            "review": "Reseña",
        }
        help_texts = {
            "name": "Ingresa el nombre del artículo.",
            "category": "Selecciona la categoría del artículo.",
            "image": "Sube una imagen del artículo.",
            "rating": "Asigna una calificación (por ejemplo, de 1 a 10).",
            "review": "Escribe una reseña para este artículo.",
        }

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 0 or rating > 10:
            raise forms.ValidationError("Rating must be between 0 and 10.")
        return rating
