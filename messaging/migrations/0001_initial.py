# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kreis',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('gehoert', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='der_kreis_ist_von_user')),
                ('mitglieder', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='der_kreis_hat_als_mitglied')),
            ],
        ),
        migrations.CreateModel(
            name='Nachricht',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('time_posted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Thema',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Direktnachricht',
            fields=[
                ('nachricht', models.OneToOneField(to='messaging.Nachricht', serialize=False, primary_key=True)),
                ('empfaenger', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='nachricht',
            name='antwort_auf',
            field=models.ForeignKey(to='messaging.Nachricht', null=True, related_name='ist_antwort_auf_nachricht'),
        ),
        migrations.AddField(
            model_name='nachricht',
            name='erwaehnt',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='die_nachricht_erwaehnt_user'),
        ),
        migrations.AddField(
            model_name='nachricht',
            name='original',
            field=models.ForeignKey(to='messaging.Nachricht', null=True, related_name='die_originalnachricht_ist'),
        ),
        migrations.AddField(
            model_name='nachricht',
            name='published_in',
            field=models.ManyToManyField(to='messaging.Kreis', related_name='die_nachricht_ist_in_kreis'),
        ),
        migrations.AddField(
            model_name='nachricht',
            name='publisher',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='die_nachricht_wurde_geschrieben_von'),
        ),
        migrations.AddField(
            model_name='nachricht',
            name='thema',
            field=models.ManyToManyField(to='messaging.Thema', related_name='die_nachricht_hat_thema'),
        ),
    ]
