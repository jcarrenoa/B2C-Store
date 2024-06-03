# Generated by Django 4.2.7 on 2024-06-03 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_evento_alter_descuento_imagen_alter_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.AutoField(primary_key=True, serialize=False)),
                ('idPerfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carritos',
                'db_table': 'Carrito',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='Descripcion',
            field=models.CharField(default='Aun no se tiene informacion del prodcuto.', max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('idOrden', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Total', models.FloatField()),
                ('Estado', models.BooleanField()),
                ('idPerfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
                'db_table': 'Orden',
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('idMensaje', models.AutoField(primary_key=True, serialize=False)),
                ('Asunto', models.CharField(max_length=50)),
                ('Mensaje', models.CharField(max_length=400)),
                ('Fecha', models.DateField()),
                ('idPerfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'db_table': 'Mensaje',
            },
        ),
        migrations.CreateModel(
            name='DetallesCarrito',
            fields=[
                ('idDetallesCarrito', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField()),
                ('idCarrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.carrito')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producto')),
            ],
            options={
                'verbose_name': 'DetallesCarrito',
                'verbose_name_plural': 'DetallesCarritos',
                'db_table': 'DetallesCarrito',
            },
        ),
    ]
