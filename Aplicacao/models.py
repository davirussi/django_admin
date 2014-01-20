# -*- coding: utf-8 -*-
from django.db import models
from datetime import *


class Proprietario(models.Model):
    TIPOS = (
        ('Casado', 'Casado'),
        ('Solteiro', 'Solteiro'),
        ('Nenhum', 'Nenhum'),
    )
    nome = models.CharField(max_length=100, verbose_name='Nome')
    telefone = models.CharField(max_length=12, default='00-000000000', verbose_name='Telefone')
    endereco = models.CharField(max_length=128, verbose_name='Endereço')
    estado_civil = models.CharField(max_length=10, choices=TIPOS, default='Nenhum', verbose_name='Estado Civil')
    conjuge = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cônjuge')

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'
        
    def __unicode__(self):
        return self.nome

class Carro(models.Model):
    ano = models.IntegerField(default='0000', verbose_name='Ano')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    numero_chassi = models.CharField(max_length=18, unique=True, verbose_name='Número do Chassi')
    cor = models.CharField(max_length=15, verbose_name='Cor')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    proprietario = models.ManyToManyField(Proprietario, through='Propriedade')

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        
    def __unicode__(self):
        return self.numero_chassi

class Propriedade(models.Model):
    proprietario = models.ForeignKey(Proprietario, verbose_name='Proprietário')
    carro = models.ForeignKey(Carro, verbose_name='Carro')
    data_compra = models.DateField(default=datetime.now, blank=True, verbose_name='Data de Compra')
    valor_compra = models.FloatField(verbose_name='Valor Pago')    
    
    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'
        unique_together = ('proprietario', 'carro','data_compra',)
    
    def __unicode__(self):
        return (unicode(self.proprietario) + ' - ' + unicode(self.carro))

