# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0076_auto_20150930_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examticket',
            options={'ordering': ('exam__course', '-creation_time'), 'verbose_name': 'Exam ticket', 'verbose_name_plural': 'Exam tickets', 'permissions': (('can_issue_exam_tickets', 'Can issue exam tickets to student'),)},
        ),
    ]
