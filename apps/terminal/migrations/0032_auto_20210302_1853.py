# Generated by Django 3.1 on 2021-03-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0031_auto_20210113_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='type',
            field=models.CharField(choices=[('koko', 'KoKo'), ('guacamole', 'Guacamole'), ('omnidb', 'OmniDB'), ('xrdp', 'Xrdp')], default='koko', max_length=64, verbose_name='type'),
        ),
    ]