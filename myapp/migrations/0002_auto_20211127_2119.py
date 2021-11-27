# Generated by Django 3.2.7 on 2021-11-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='memory_usage',
            field=models.CharField(blank=True, choices=[('n', '  '), ('4GB', '4GB'), ('16GB', '16GB')], default='n', max_length=25, null=True),
        ),
    ]
