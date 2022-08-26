# Generated by Django 4.1 on 2022-08-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('User_Cedula', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('User_Nombre', models.CharField(max_length=50)),
                ('User_Apellidos', models.CharField(max_length=50)),
                ('User_Tel', models.CharField(max_length=10)),
                ('User_Direccion', models.CharField(max_length=80)),
                ('User_Email', models.EmailField(max_length=70)),
                ('User_Rol', models.CharField(max_length=25)),
                ('User_Passwd', models.CharField(max_length=30)),
                ('User_Status', models.CharField(max_length=1)),
            ],
        ),
    ]