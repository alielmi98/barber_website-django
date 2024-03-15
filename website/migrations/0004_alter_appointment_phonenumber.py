# Generated by Django 4.2.9 on 2024-03-14 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_appointment_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phoneNumber',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{10,11}$')]),
        ),
    ]
