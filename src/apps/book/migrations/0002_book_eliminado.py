# Generated by Django 4.0.4 on 2022-05-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
    ]
