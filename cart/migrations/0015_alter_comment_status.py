# Generated by Django 3.2 on 2021-07-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10),
        ),
    ]
