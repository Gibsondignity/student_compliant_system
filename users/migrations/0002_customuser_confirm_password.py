# Generated by Django 4.2.5 on 2023-09-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirm_password',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
