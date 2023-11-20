# Generated by Django 4.2.6 on 2023-10-22 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('block_number', models.CharField(max_length=10)),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
                'db_table': 'property_detail',
            },
        ),
        migrations.CreateModel(
            name='PropertyBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(max_length=10)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rent_charged', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rent_due_date', models.DateField()),
                ('block', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.property')),
            ],
            options={
                'verbose_name_plural': 'PropertyBlocks',
                'db_table': 'block_detail',
            },
        ),
    ]
