# Generated by Django 3.0.5 on 2020-08-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_delete_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('scale', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
            ],
        ),
    ]
