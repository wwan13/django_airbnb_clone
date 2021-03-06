# Generated by Django 2.2.5 on 2020-08-18 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200818_2220'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Amenities',
            new_name='Amenity',
        ),
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Room Type'},
        ),
        migrations.AlterModelOptions(
            name='rule',
            options={'verbose_name': 'House Rule'},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='ameity',
            new_name='ameities',
        ),
        migrations.AlterField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='rooms.Facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='house_rule',
            field=models.ManyToManyField(blank=True, to='rooms.Rule'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
