# Generated by Django 5.0.3 on 2024-03-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.CharField(blank=True, choices=[('Heavy duty and light vehicle ', 'Heavy duty and light vehicle'), ('Plant', 'Plant'), ('Surface mining ', 'Surface mining '), ('Finance (support services)', 'Finance (support services)'), ('Underground', 'Underground'), ('Security and safety department ', 'Security and safety department '), ('Primus(canteen)', 'Primus(canteen)'), ('Environment department', 'Environment department')], max_length=124, null=True),
        ),
    ]
