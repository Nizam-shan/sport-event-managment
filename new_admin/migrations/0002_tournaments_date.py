# Generated by Django 4.1 on 2022-08-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournaments',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
