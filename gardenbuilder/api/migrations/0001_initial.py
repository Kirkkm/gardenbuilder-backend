# Generated by Django 3.1 on 2020-08-16 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('length', models.PositiveSmallIntegerField(default=0)),
                ('width', models.PositiveSmallIntegerField(default=0)),
                ('notes', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('square_footage', models.DecimalField(decimal_places=2, default=0.25, max_digits=3)),
                ('square_footage_sfg', models.DecimalField(decimal_places=2, default=0.25, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('xLocation', models.PositiveSmallIntegerField(default=0)),
                ('yLocation', models.PositiveSmallIntegerField(default=0)),
                ('bed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='api.bed')),
            ],
        ),
        migrations.CreateModel(
            name='PlantVariety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('plant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant_varieties', to='api.plant')),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='api.section'),
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('garden_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gardens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='bed',
            name='garden_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds', to='api.garden'),
        ),
    ]
