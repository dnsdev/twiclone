# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_auto_20150504_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kreis',
            name='mitglieder',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='der_kreis_hat_als_mitglied'),
        ),
        migrations.AlterField(
            model_name='nachricht',
            name='antwort_auf',
            field=models.ForeignKey(null=True, to='messaging.Nachricht', blank=True, related_name='ist_antwort_auf_nachricht'),
        ),
        migrations.AlterField(
            model_name='nachricht',
            name='erwaehnt',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='die_nachricht_erwaehnt_user'),
        ),
        migrations.AlterField(
            model_name='nachricht',
            name='original',
            field=models.ForeignKey(null=True, to='messaging.Nachricht', blank=True, related_name='die_originalnachricht_ist'),
        ),
        migrations.AlterField(
            model_name='nachricht',
            name='published_in',
            field=models.ManyToManyField(blank=True, to='messaging.Kreis', related_name='die_nachricht_ist_in_kreis'),
        ),
        migrations.AlterField(
            model_name='nachricht',
            name='thema',
            field=models.ManyToManyField(blank=True, to='messaging.Thema', related_name='die_nachricht_hat_thema'),
        ),
    ]
