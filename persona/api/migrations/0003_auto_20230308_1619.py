# Generated by Django 3.2.1 on 2023-03-08 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230308_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='surname',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='name',
            new_name='nombre',
        ),
    ]
