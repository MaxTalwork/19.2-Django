from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProdForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter',)

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        name = self.cleaned_data['name']
        for word in forbidden_words:
            if word in name:
                raise ValidationError('Название содержит недопустимые слова')
        return name

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        description = self.cleaned_data['description']
        for word in forbidden_words:
            if word in description:
                raise ValidationError('Описание содержит недопустимые слова')
        return description


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
