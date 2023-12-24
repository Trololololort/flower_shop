from django import forms
from .models import Category, Goods
from .const import CHOICES_DICT




def get_choices():
    choices = [(k, v) for k, v in CHOICES_DICT.items()]
    return choices

class GoodsSortFilterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False


    order_by = forms.ChoiceField(choices=get_choices, label="Сортировать по:", required=False)

    class Meta:
        model = Goods

        fields = ["category", ]
