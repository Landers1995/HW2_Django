from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name').lower()

        for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if i in cleaned_data:
                raise ValueError('При создании товара нельзя использовать слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description').lower()

        for i in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if i in cleaned_data:
                raise ValueError(
                    'При создании товара нельзя использовать слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.')

        return cleaned_data
