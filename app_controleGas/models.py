from datetime import date
from tabnanny import verbose
from django.db import models
from django.forms import DateTimeField
from stdimage.models import StdImageField

class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    atualizado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    class Meta:
        abstract = True


class Apartamento(Base):
    apartamento = models.CharField('Apartamento', max_length=4)
    class Meta:
        verbose_name = 'Apartamento'
        verbose_name_plural = 'Apartamentos'
    
    def __str__(self):
        return self.apartamento      


class Leitura(Base):
    MES_CHOICES = (
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    )
    apartamento = models.ForeignKey('app_controleGas.Apartamento', verbose_name='Apartamento', on_delete=models.CASCADE)
    data = models.DateTimeField('Data do Lançameto', auto_now_add=True)
    mes = models.CharField('Mês Referência', max_length=20, choices=MES_CHOICES, default='Falta Preencher...')
    leitura = models.IntegerField('Leitura', default=0)
    
    class Meta:
        verbose_name = 'Leitura'
        verbose_name_plural = 'Leiuras'
    
    def __str__(self):
        return self.mes


        """
         AP_CHOICES = (
        ('101', '101')
        ('102', '102')
        ('201', '201')
        ('202', '202')
        ('301', '301')
        ('302', '302')
        ('401', '401')
        ('402', '402')
        ('501', '501')
        ('502', '502')
        ('601', '601')
        ('602', '602')
        ('701', '701')
        ('702', '702')
        ('801', '801')
        ('802', '802')
        ('901', '901')
        ('902', '902')
        ('1001', '1001')
        ('1002', '1002')
        ('1101', '1101')
        ('1102', '1102')
        ('1201', '1201')
        ('1202', '1202')
        ('1301', '1301')
        ('1302', '1302')
        ('1401', '1401')
        ('1402', '1402')
        ('1501', '1501')
        ('1502', '1502')
        ('1601', '1601')
        ('1602', '1602')
        ('1701', '1701')
        ('1702', '1702')
        ('1801', '1801')
        ('1802', '1802')
        ('1901', '1901')
        ('1902', '1902')
        ('2001', '2001')
        ('2002', '2002')
        ('2101', '2101')
        ('2102', '2102')
        ('2201', '2201')
        ('2202', '2202')
        ('2301', '2301')
        ('2302', '2302')
        ('2401', '2401')
        ('2402', '2402')
        ('2501', '2501')
        ('2502', '2502')
        ('2601', '2601')
        ('2602', '2602')
        ('2701', '2701')
    )
        """
