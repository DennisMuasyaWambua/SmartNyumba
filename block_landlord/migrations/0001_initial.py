# Generated by Django 4.2.6 on 2023-10-22 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockLandlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('id_number', models.CharField(max_length=9)),
                ('is_active', models.IntegerField(default=0)),
                ('approver', models.EmailField(max_length=254)),
                ('property', models.ManyToManyField(related_name='property', to='properties.property')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'block_landlord',
            },
        ),
    ]