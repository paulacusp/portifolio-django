# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('city', models.CharField(max_length=200, verbose_name='Cidade')),
                ('zip_code', models.CharField(max_length=50, verbose_name='Cep')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('mobile', models.CharField(max_length=20, verbose_name='Celular')),
                ('about', models.TextField(max_length=300, verbose_name='Sobre')),
                ('birth_date', models.CharField(default='01 de janeiro de 1900', max_length=100, verbose_name='Data de nascimento')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('knowledge', models.TextField(max_length=300, verbose_name='Conhecimentos')),
                ('github', models.CharField(default='https://github.com/paulacusp', max_length=100, verbose_name='github')),
                ('current_position', models.CharField(max_length=50, verbose_name='Cargo atual')),
                ('company', models.CharField(max_length=50, verbose_name='Empresa')),
            ],
        ),
    ]