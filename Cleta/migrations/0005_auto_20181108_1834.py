# Generated by Django 2.1.2 on 2018-11-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cleta', '0004_auto_20181108_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='foto_perfil',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]