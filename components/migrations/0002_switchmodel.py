# Generated by Django 3.1 on 2020-08-21 16:06

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwitchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', simplepro.components.fields.SwitchField(default=False, help_text='继承自BooleanField', verbose_name='复选框')),
            ],
            options={
                'verbose_name': 'Switch切换',
                'verbose_name_plural': 'Switch切换',
            },
        ),
    ]