# Generated by Django 3.0.6 on 2020-05-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenURL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorten',
            name='slug',
            field=models.SlugField(default=12, unique=True, verbose_name="Lien de l'URL"),
            preserve_default=False,
        ),
    ]
