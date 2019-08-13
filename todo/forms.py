from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
# Meta helps Django to know where this is to be saved later
    class Meta:
        model = Item
        fields = ('name', 'done')