# Generated by Django 3.0.5 on 2020-04-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200419_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_pics'),
        ),
    ]
