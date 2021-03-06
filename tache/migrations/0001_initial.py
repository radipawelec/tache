# Generated by Django 2.2.1 on 2019-06-02 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=100, verbose_name='Name')),
                ('list_description', models.TextField(blank=True, verbose_name='Description')),
                ('list_active_status', models.BooleanField(default=True, verbose_name='Active')),
                ('list_create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('list_modify_date', models.DateTimeField(auto_now=True, verbose_name='Last activity')),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Lists',
            },
        ),
        migrations.CreateModel(
            name='ListCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=100)),
                ('card_description', models.TextField(blank=True)),
                ('card_active_status', models.BooleanField(default=True)),
                ('card_priority', models.IntegerField(choices=[(1, 'Normal'), (2, 'High'), (3, 'ASAP'), (4, 'NOW')], default=1)),
                ('card_create_date', models.DateTimeField(auto_now_add=True)),
                ('card_modify_date', models.DateTimeField(auto_now=True)),
                ('card_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tache.BoardList')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]
