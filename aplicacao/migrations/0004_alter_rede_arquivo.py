# Generated by Django 4.1.7 on 2023-04-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0003_artigo_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rede',
            name='arquivo',
            field=models.FileField(upload_to='redes'),
        ),
    ]