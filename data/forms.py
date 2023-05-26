from django.forms import ModelForm, TextInput
from .models import Store


class StoreForm(ModelForm):


    class Meta:
        model = Store
        fields = ['id_store', 'id_dr', 'id_ph', 'price', 'amount']

        widgets = {
            "id_dr": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лекарство'
            }),
            "id_ph": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Аптека'
            }),

            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),

            "amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
        }
