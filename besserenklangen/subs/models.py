from django.db import models

class Track(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    date = models.DateTimeField()

    def __unicode__(self):
        return "%s %s" % (self.id, self.date)

class Feed(models.Model):
    username = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track)

    def __unicode__(self):
        return "%d" % self.tracks.first().id