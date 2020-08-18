# Generated by Django 2.2.5 on 2020-08-18 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_abstractitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.AbstractItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('rooms.abstractitem',),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ManyToManyField(blank=True, to='rooms.RoomType'),
        ),
    ]