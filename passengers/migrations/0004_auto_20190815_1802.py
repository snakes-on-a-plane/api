# Generated by Django 2.2.4 on 2019-08-15 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passengers', '0003_carryon_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carryon',
            old_name='item',
            new_name='passenger',
        ),
    ]