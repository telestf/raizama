# Generated by Django 2.2.4 on 2019-11-06 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('razao_social', models.CharField(max_length=40)),
                ('cnpj', models.CharField(max_length=40)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('tipo', models.ManyToManyField(related_name='produtor_tipo', to='content.Tipo')),
            ],
        ),
    ]
