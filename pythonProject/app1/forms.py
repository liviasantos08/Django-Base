from django import forms

from django.forms.widgets import NumberInput
from django.urls import reverse_lazy

from app1.models import Pessoa
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class PessoaForms(forms.ModelForm):
    data_nascimento = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=NumberInput(attrs={'type': 'time'}))
    gol = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-6 mb-0'),
                Column('sobrenome', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'telefone',
            'cpf',
            Row(
                Column('data_nascimento', css_class='form-group col-md-6 mb-0'),
                Column('hora', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'genero',
            'gol',
            Submit('submit', 'Salva')
        )

    class Meta:
        model = Pessoa
        fields = '__all__'

