# Generated by Django 4.2.10 on 2024-02-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='department',
            field=models.CharField(blank=True, choices=[('Heavy duty and light vehicle ', 'Heavy duty and light vehicle'), ('Plant', 'Plant'), ('Surface mining ', 'Surface mining '), ('Finance (support services)', 'Finance (support services)'), ('Underground', 'Underground'), ('Security and safety department ', 'Security and safety department '), ('Primus(canteen)', 'Primus(canteen)'), ('Environment department', 'Environment department')], max_length=124, null=True),
        ),
    ]