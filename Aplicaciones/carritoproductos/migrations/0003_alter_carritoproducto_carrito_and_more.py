# Generated by Django 5.2.1 on 2025-07-06 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_alter_carrito_usuario'),
        ('carritoproductos', '0002_alter_carritoproducto_carrito'),
        ('productos', '0002_remove_producto_imagen_url_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritoproducto',
            name='carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productos_en_carrito', to='carrito.carrito'),
        ),
        migrations.AlterField(
            model_name='carritoproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto'),
        ),
    ]
