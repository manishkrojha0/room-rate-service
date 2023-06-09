# Generated by Django 4.2.2 on 2023-06-06 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_id', models.PositiveIntegerField(unique=True)),
                ('discount_name', models.CharField(max_length=200)),
                ('discount_type', models.CharField(choices=[('FIXED', 'Fixed'), ('PERCENTANGE', 'Percentage')], default='FIXED', max_length=250)),
                ('discount_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='RoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(unique=True)),
                ('room_name', models.CharField(max_length=250)),
                ('default_rate', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='OverriddenRoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overridden_room_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('stay_date', models.DateField()),
                ('room_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='over_ridden_rate', to='core.roomrate')),
            ],
        ),
    ]
