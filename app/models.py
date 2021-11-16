#--*************************************************************
#--FEITO POR VICKSTUFF, 2021 - https://github.com/Victoria-Belo
#--*************************************************************
from django.db import models

class Base(models.Model):
    at_create = models.DateTimeField(auto_now_add=True)
    at_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Produto(Base):
    name = models.CharField(max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=7)
    inventory = models.IntegerField()

    class Meta:
        ordering = ['name', 'value', 'inventory', 'at_create', 'at_update']

    def __str__(self):
        return self.name


class Cliente(Base):
    cpf = models.IntegerField(null=False)
    firstname = models.CharField(max_length=80, blank=False)
    lastname = models.CharField(max_length=80, blank=False)
    email = models.EmailField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['cpf', 'firstname', 'lastname', 'email', 'address', 'at_create', 'at_update']

    def __str__(self):
        return f'{self.firstname} {self.lastname}'





























#--*************************************************************
#--FEITO POR VICKSTUFF, 2021 - https://github.com/Victoria-Belo
#--*************************************************************