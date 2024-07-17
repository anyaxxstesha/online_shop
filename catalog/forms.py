from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    @staticmethod
    def check_restrictions(field, field_name):
        restrictions = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                        'бесплатно', 'обман', 'полиция', 'радар']  # Запрещенные слова
        for word in restrictions:
            if word in field:
                raise forms.ValidationError(f"В поле {field_name} присутствует запрещенное слово: {word}")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.check_restrictions(name, 'name')

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.check_restrictions(description, 'description')

        return description
