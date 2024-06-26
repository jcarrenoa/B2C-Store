# Generated by Django 4.2.7 on 2024-05-29 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('ProductoOfrecido', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.IntegerField()),
                ('Tamaño', models.CharField(max_length=50, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='images')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('idDescuento', models.AutoField(primary_key=True, serialize=False)),
                ('PorcentajeDesc', models.IntegerField()),
                ('FechaInicio', models.DateField()),
                ('FechaFinal', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='otros')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producto')),
            ],
            options={
                'verbose_name': 'Descuento',
                'verbose_name_plural': 'Descuentos',
                'db_table': 'Descuento',
            },
        ),
    ]
