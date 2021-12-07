# Generated by Django 3.2 on 2021-12-03 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(blank=True, max_length=120)),
                ('longname', models.CharField(blank=True, max_length=120)),
                ('route_type', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='StationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('digital_address', models.CharField(blank=True, max_length=200)),
                ('master_info', models.FileField(blank=True, upload_to='')),
                ('contact', models.CharField(blank=True, max_length=120)),
                ('photo', models.ImageField(blank=True, upload_to='station_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('lat', models.PositiveIntegerField()),
                ('long', models.PositiveIntegerField()),
                ('digital_address', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headsign', models.CharField(max_length=120)),
                ('note', models.TextField(blank=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ttliveapp.routes')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ttliveapp.stationmodel')),
            ],
        ),
        migrations.AddField(
            model_name='routes',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ttliveapp.stationmodel'),
        ),
        migrations.CreateModel(
            name='MissingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('origin', models.CharField(blank=True, max_length=120)),
                ('drop_point', models.CharField(blank=True, max_length=120)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ttliveapp.stationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FareRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(blank=True, max_length=120)),
                ('destination', models.CharField(blank=True, max_length=120)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ttliveapp.routes')),
            ],
        ),
    ]