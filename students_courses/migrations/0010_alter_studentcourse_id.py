# Generated by Django 5.0.4 on 2024-05-08 14:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_courses', '0009_alter_studentcourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
