# Generated by Django 3.0.5 on 2020-08-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(),
        ),
    ]
