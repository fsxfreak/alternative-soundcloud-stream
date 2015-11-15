from django.db import models

class Track(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.id

class Feed(models.Model):
    tracks = models.ManyToManyField(Track)

    def __unicode__(self):
        return ', '.join(self.tracks.all().id)