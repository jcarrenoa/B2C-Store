# Generated by Django 4.2.7 on 2024-05-29 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_proveedor_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='idProveedor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.proveedor'),
            preserve_default=False,
        ),
    ]
