# Generated by Django 5.0.4 on 2024-05-08 14:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_alter_content_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d401418a-5e4a-4aca-9ac7-375615ba4d18'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]