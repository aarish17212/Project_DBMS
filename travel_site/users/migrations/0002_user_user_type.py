# Generated by Django 3.0.5 on 2020-04-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.TextField(choices=[('Airline', 'Airline'), ('Bus', 'Bus'), ('Hotel', 'Hotel'), ('Customer', 'Customer')], default='Customer'),
        ),
    ]
