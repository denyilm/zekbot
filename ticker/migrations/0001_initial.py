# Generated by Django 3.2 on 2022-01-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eth',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('price', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
