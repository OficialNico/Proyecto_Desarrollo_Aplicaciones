# Generated by Django 4.2.3 on 2023-07-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lavado_Vehiculos', '0004_customuser_factura_remove_agendar_hora_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendar_hora',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
    ]
