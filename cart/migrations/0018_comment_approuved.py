# Generated by Django 3.2 on 2021-07-26 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_auto_20210726_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approuved',
            field=models.BooleanField(default=False),
        ),
    ]