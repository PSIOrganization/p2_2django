# Generated by Django 3.2.1 on 2023-03-08 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='persona',
            name='person_id',
        ),
    ]