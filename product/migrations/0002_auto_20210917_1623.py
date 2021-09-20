# Generated by Django 3.2.3 on 2021-09-17 16:23

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('available', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='product',
            name='internal_code',
            field=models.IntegerField(null=True, verbose_name='Código Interno'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Produto', max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade'),
        ),
    ]