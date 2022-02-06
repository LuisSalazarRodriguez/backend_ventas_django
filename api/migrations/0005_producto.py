# Generated by Django 3.2 on 2022-02-06 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('producto_descripcion', models.CharField(max_length=100, verbose_name='desscripcion del producto')),
                ('producto_precio', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='precio del producto')),
                ('producto_estado', models.CharField(max_length=10, verbose_name='estado producto')),
                ('linea_codigo', models.ForeignKey(db_column='linea_codigo', on_delete=django.db.models.deletion.RESTRICT, related_name='Producto', to='api.linea', verbose_name='Linea')),
                ('marca_codigo', models.ForeignKey(db_column='marca_codigo', on_delete=django.db.models.deletion.RESTRICT, related_name='Producto', to='api.marca', verbose_name='Marca')),
                ('moneda_codigo', models.ForeignKey(db_column='moneda_codigo', on_delete=django.db.models.deletion.RESTRICT, related_name='Producto', to='api.moneda', verbose_name='Moneda')),
                ('um_codigo', models.ForeignKey(db_column='um_codigo', on_delete=django.db.models.deletion.RESTRICT, related_name='Producto', to='api.unidadmedida', verbose_name='UnidadMedida')),
            ],
        ),
    ]
