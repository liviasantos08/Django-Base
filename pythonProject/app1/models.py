from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cpf_field.models import CPFField

GENER = [('feminino', 'Feminino'), ('masculino', 'Masculino')]


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = PhoneNumberField()
    cpf = CPFField('cpf')
    data_nascimento = models.DateField()
    hora = models.TimeField()
    genero = models.CharField(max_length=50, choices=GENER)
    gol = models.BooleanField(default=False)





