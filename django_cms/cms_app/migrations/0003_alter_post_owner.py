# Generated by Django 4.2.3 on 2023-07-22 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0002_cmsuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='cms_app.cmsuser'),
        ),
    ]
