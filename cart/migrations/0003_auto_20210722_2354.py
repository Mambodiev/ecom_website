# Generated by Django 3.2 on 2021-07-22 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='primary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_products', to='cart.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='secondary_categories',
            field=models.ManyToManyField(blank=True, to='cart.Category'),
        ),
    ]
