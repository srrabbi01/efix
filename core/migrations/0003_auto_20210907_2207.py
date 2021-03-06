# Generated by Django 3.2 on 2021-09-07 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_servicerequest_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='created_at',
        ),
        migrations.AddField(
            model_name='invoice',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
