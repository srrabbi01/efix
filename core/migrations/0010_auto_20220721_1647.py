# Generated by Django 3.2.13 on 2022-07-21 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_customuserregistration_work_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserregistration',
            name='role',
            field=models.CharField(choices=[('customer', 'customer'), ('technician', 'technician')], default='customer', max_length=122, null=True),
        ),
        migrations.CreateModel(
            name='NotificationToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_token', models.CharField(max_length=999, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userdevicetoken', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
