# Generated by Django 3.2 on 2022-01-08 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0002_auto_20220105_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('eth', models.FloatField(blank=True, null=True)),
                ('shib', models.FloatField(blank=True, null=True)),
                ('para', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('pair', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('profit', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]