# Generated by Django 4.2.7 on 2024-06-01 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_b2c', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='portada',
            field=models.ImageField(default='perfil/portadauser.jpg', null=True, upload_to='portada/%Y/%m/%d'),
        ),
    ]
