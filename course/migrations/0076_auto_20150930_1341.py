# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0075_course_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(help_text="A human-readable course number/ID for the course (e.g. 'CS123')", max_length=200, null=True),
        ),
    ]
