# Generated by Django 4.1.4 on 2022-12-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('moneda', models.CharField(max_length=20)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
