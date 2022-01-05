# Generated by Django 3.2 on 2022-01-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shib',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('pair', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='eth',
            name='pair',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]