# Generated by Django 4.1 on 2022-08-25 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_alter_transacciones_tra_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas',
            name='CU_CEDULACLI',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='CU_TP',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='NUMEROCUENTA',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
