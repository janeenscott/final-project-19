# Generated by Django 2.1.7 on 2019-03-22 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190321_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='buddy',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
