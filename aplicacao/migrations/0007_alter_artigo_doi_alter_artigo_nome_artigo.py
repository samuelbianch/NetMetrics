# Generated by Django 4.1.7 on 2024-05-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0006_alter_rede_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='doi',
            field=models.TextField(blank=True, help_text='Link para acesso ao trabalho'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='nome_artigo',
            field=models.CharField(max_length=200),
        ),
    ]
