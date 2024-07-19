from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
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


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ("product", "version_number", "version_name", "is_current_version")


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("description", "category", "is_published")
