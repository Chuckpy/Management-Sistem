# Generated by Django 3.2.3 on 2021-09-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', to='dashboard.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='internal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
