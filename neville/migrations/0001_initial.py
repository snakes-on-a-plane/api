# Generated by Django 2.2.4 on 2019-08-15 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passengers', '0007_delete_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('quote', models.CharField(max_length=1024)),
                ('carry_on', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='carry_on', to='passengers.CarryOn')),
                ('personal_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='personal_item', to='passengers.CarryOn')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
