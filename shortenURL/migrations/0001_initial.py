# Generated by Django 3.0.6 on 2020-05-21 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shorten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL à réduire')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name="Date d'enregistrement")),
                ('nb_acces', models.IntegerField(default=0, verbose_name='Nombre de vues')),
            ],
            options={
                'verbose_name': "Raccourcisseur d'URL",
                'verbose_name_plural': "Raccourcisseurs d'URL",
            },
        ),
    ]
