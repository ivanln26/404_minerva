# Generated by Django 3.2.3 on 2021-05-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerva', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='vendor',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
