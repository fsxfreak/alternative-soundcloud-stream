from django.db import models

class Track(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=50, default='in the end')
    artist = models.CharField(max_length=50, default='linking parking')
    uri = models.CharField(max_length=100, default='localhost')
    art = models.CharField(max_length=100, editable=False, default='http://i.imgur.com/BNBFGfg.jpg')

    def __unicode__(self):
        return "%s - %s" % (self.artist, self.title)

class Feed(models.Model):
    username = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track)

    def __unicode__(self):
        return "%s" % self.username