# Generated by Django 3.0.5 on 2020-08-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(default='city', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='zip_code',
            field=models.CharField(default='12345', max_length=50),
            preserve_default=False,
        ),
    ]
