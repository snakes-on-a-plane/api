# Generated by Django 2.2.4 on 2019-08-15 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passengers', '0007_delete_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeGs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('accessories', models.CharField(max_length=256)),
                ('carry_on', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='carry_on', to='passengers.CarryOn')),
                ('personal_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='personal_item', to='passengers.CarryOn')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
