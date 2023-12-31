# Generated by Django 4.2.5 on 2023-10-02 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, choices=[('Finance and Account', 'Finance and Account'), ('Faculty of Engineering ', 'Faculty of Engineering'), ('Faculty of Computing and Information System(FoCIS)', 'Faculty of Computing and Information System(FoCIS)'), ('Business school ', 'Business school'), ('Security', 'Security'), ('Library', 'Library'), ('Student Affairs', 'Student Affairs')], max_length=124, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
