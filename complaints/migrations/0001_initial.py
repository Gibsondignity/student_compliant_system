# Generated by Django 4.2.5 on 2023-10-02 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Enter your complaint')),
                ('details', models.TextField(blank=True, verbose_name='Explain in more detail')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(blank=True, choices=[('Class Room', 'Class Room'), ('Campus', 'Campus'), ('Library', 'Library'), ('Administration', 'Administration')], default='Campus', max_length=64)),
                ('department', models.CharField(blank=True, choices=[('Finance and Account', 'Finance and Account'), ('Faculty of Engineering ', 'Faculty of Engineering'), ('Faculty of Computing and Information System(FoCIS)', 'Faculty of Computing and Information System(FoCIS)'), ('Business school ', 'Business school'), ('Security', 'Security'), ('Library', 'Library'), ('Student Affairs', 'Student Affairs')], max_length=124, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Solved', 'Solved')], default='Pending', max_length=24)),
                ('comment', models.CharField(blank=True, default='', max_length=265)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=120)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.complaint')),
            ],
        ),
    ]
