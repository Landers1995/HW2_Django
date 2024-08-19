from django import forms
from django.forms import BooleanField
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if i in cleaned_data.lower():
                raise ValueError('При создании товара нельзя использовать слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.'
                )

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if i in cleaned_data.lower():
                raise ValueError(
                    'При создании товара нельзя использовать слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.'
                )

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
