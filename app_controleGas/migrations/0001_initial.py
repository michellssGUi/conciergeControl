# Generated by Django 4.0.5 on 2022-06-22 20:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('apartamento', models.CharField(max_length=4, verbose_name='Apartamento')),
            ],
            options={
                'verbose_name': 'Apartamento',
                'verbose_name_plural': 'Apartamentos',
            },
        ),
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('data', models.DateTimeField(default=datetime.date, verbose_name='Data')),
                ('mes', models.CharField(choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'), ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Dezembro', 'Dezembro')], default='Falta Preencher...', max_length=20, verbose_name='Mês Referência')),
                ('leitura', models.IntegerField(default=0, verbose_name='Leitura')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_controleGas.apartamento', verbose_name='Apartamento')),
            ],
            options={
                'verbose_name': 'Leitura',
                'verbose_name_plural': 'Leiuras',
            },
        ),
    ]
