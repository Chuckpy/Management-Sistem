# Generated by Django 3.2.3 on 2021-09-11 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_sale_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.CreateModel(
            name='SaleItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sale')),
            ],
        ),
    ]
