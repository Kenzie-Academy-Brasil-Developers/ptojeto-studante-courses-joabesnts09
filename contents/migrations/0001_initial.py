# Generated by Django 5.0.4 on 2024-05-01 15:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('8e71e44b-8fb8-4700-8b07-438b921a0d19'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('video_url', models.CharField(max_length=200)),
            ],
        ),
    ]
