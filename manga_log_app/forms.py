from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "category", "image", "rating", "review"]

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 0 or rating > 10:
            raise forms.ValidationError("Rating must be between 0 and 10.")
        return rating
