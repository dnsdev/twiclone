# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20150504_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kreis',
            name='mitglieder',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='der_kreis_hat_als_mitglied'),
        ),
    ]
