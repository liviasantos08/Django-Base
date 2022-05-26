from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from .forms import PessoaForms
from .models import Pessoa


class Base(View):
    template = 'base.html'

    def get(self, request):
        return render(request, self.template)


class PessoaCreate(CreateView):
    model = Pessoa
    form_class = PessoaForms
    template_name = 'forms.html'
    success_url = reverse_lazy('tabela')


class PessoaList(ListView):
    model = Pessoa
    template_name = "tabela.html"
