# Generated by Django 3.2.3 on 2021-05-30 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minerva', '0006_auto_20210529_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='create_at',
            new_name='created_at',
        ),
    ]