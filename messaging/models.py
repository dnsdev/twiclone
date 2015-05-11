from django.db import models
from django.contrib.auth.models import User


class Kreis(models.Model):
    name = models.CharField(max_length=140, null=False)
    gehoert = models.ForeignKey(User, null=False, related_name="der_kreis_ist_von_user")
    mitglieder = models.ManyToManyField(User, blank=True, related_name="der_kreis_hat_als_mitglied")


class Thema(models.Model):
    name = models.CharField(max_length=140, primary_key=True)


class NachrichtManager(models.Manager):

    def all_available(self):
        """
        get all messages available to user.
        that means, that only messages get returned, that user did not published, but are available, because he is
        in the "kreis" where the message was published to.
        :return:
        """
        return None
    def all(self):
        return super(NachrichtManager, self).filter(direktnachricht__isnull = True)
    def all_direktnachrichten(self):
        return super(NachrichtManager, self).filter(direktnachricht__isnull = False)


class Nachricht(models.Model):
    text = models.CharField(null=False, max_length=140)
    time_posted = models.DateTimeField(null=False)
    antwort_auf = models.ForeignKey("self", blank=True, null=True, related_name="ist_antwort_auf_nachricht")
    original = models.ForeignKey("self", blank=True, null=True, related_name="die_originalnachricht_ist")
    publisher = models.ForeignKey(User, null=False, related_name="die_nachricht_wurde_geschrieben_von")
    erwaehnt = models.ManyToManyField(User, blank=True, related_name="die_nachricht_erwaehnt_user")
    published_in = models.ManyToManyField(Kreis, blank=True, related_name="die_nachricht_ist_in_kreis")
    thema = models.ManyToManyField(Thema, blank=True, related_name="die_nachricht_hat_thema")

    objects = NachrichtManager()
    all_objects = models.Manager()

    def __str__(self):
        return "N: " + self.text


class Direktnachricht(models.Model):
    nachricht = models.OneToOneField(Nachricht, primary_key=True)
    empfaenger = models.ForeignKey(User, null=False)
    def __str__(self):
        return "DN: " + self.nachricht.text