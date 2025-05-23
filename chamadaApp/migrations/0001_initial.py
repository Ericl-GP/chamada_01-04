# Generated by Django 5.1.7 on 2025-04-02 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome_categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id_plano', models.AutoField(primary_key=True, serialize=False)),
                ('nome_plano', models.CharField(max_length=200, null=True)),
                ('valor_plano', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id_telefone', models.AutoField(primary_key=True, serialize=False)),
                ('numero_telefone', models.CharField(max_length=200)),
                ('tipo_telefone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(blank=True, max_length=200, null=True)),
                ('foto_cliente', models.ImageField(blank=True, null=True, upload_to='')),
                ('cpf_cliente', models.CharField(max_length=200)),
                ('email_cliente', models.CharField(max_length=200, null=True)),
                ('id_categoria', models.ForeignKey(blank=True, db_column='id_categoria', on_delete=django.db.models.deletion.DO_NOTHING, to='chamadaApp.categoria')),
                ('id_plano', models.ForeignKey(blank=True, db_column='id_plano', on_delete=django.db.models.deletion.DO_NOTHING, to='chamadaApp.plano')),
                ('id_telefone', models.ForeignKey(blank=True, db_column='id_telefone', on_delete=django.db.models.deletion.DO_NOTHING, to='chamadaApp.telefone')),
            ],
        ),
    ]
