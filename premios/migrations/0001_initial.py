# Generated by Django 5.0.6 on 2024-07-17 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Premio', models.CharField(max_length=50)),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to='premios/')),
                ('Valor', models.IntegerField(default=0)),
            ],
        ),
    ]
