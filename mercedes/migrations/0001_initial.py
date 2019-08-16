# Generated by Django 2.2.4 on 2019-08-15 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passengers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mercedes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('quote', models.CharField(max_length=1024)),
                ('money', models.CharField(default=None, max_length=10)),
                ('carry_on', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='carry_on', to='passengers.CarryOn')),
                ('personal_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='personal_item', to='passengers.CarryOn')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]