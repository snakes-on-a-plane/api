# Generated by Django 2.2.4 on 2019-08-15 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mercedes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercedes',
            name='personal_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='personal_item', to='passengers.CarryOn'),
        ),
    ]
