# Generated by Django 5.0.4 on 2024-05-02 01:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_courses', '0002_alter_studentcourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9817ae71-13bf-4efb-a258-15be7b2408b3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
