from django.db import models
from django.contrib.auth.models import User


class Kreis(models.Model):
    name = models.CharField(max_length=140, null=False)
    gehoert = models.ForeignKey(User, null=False, related_name="der_kreis_ist_von_user")
    mitglieder = models.ManyToManyField(User, blank=True, related_name="der_kreis_hat_als_mitglied")


class Thema(models.Model):
    name = models.CharField(max_length=140, primary_key=True)


class Nachricht(models.Model):
    text = models.CharField(null=False, max_length=140)
    time_posted = models.DateTimeField(null=False)
    antwort_auf = models.ForeignKey("self", blank=True, null=True, related_name="ist_antwort_auf_nachricht")
    original = models.ForeignKey("self", blank=True, null=True, related_name="die_originalnachricht_ist")
    publisher = models.ForeignKey(User, null=False, related_name="die_nachricht_wurde_geschrieben_von")
    erwaehnt = models.ManyToManyField(User, blank=True, related_name="die_nachricht_erwaehnt_user")
    published_in = models.ManyToManyField(Kreis, blank=True, related_name="die_nachricht_ist_in_kreis")
    thema = models.ManyToManyField(Thema, blank=True, related_name="die_nachricht_hat_thema")


class Direktnachricht(models.Model):
    nachricht = models.OneToOneField(Nachricht, primary_key=True)
    empfaenger = models.ForeignKey(User, null=False)