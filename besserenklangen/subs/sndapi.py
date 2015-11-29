from soundcloud_secret import *
from pprint import pprint
from datetime import timedelta, date
from dateutil import parser

import soundcloud

def build_feed(username):
    client = soundcloud.Client(client_id='58b4b27103ca13cfc7675ca4bb6f9a5d')

    id = client.get('/resolve', url='http://soundcloud.com/%s/' % username).id
    count = client.get('users/%s/' % id).followings_count
    followings_raw = client.get('users/%s/followings' % id, limit=count)
    followings = map(lambda artist: artist.id, followings_raw)

    recency = timedelta(days = 2)
    oldest = date.today() - recency
    oldest_fmtted = { 'from': '%u-%u-%u 00:00:00' % (oldest.year, oldest.month, oldest.day) }

    recent_tracks = []

    for artist in followings:
        raw_tracks = client.get('users/%s/tracks' % artist, created_at=oldest_fmtted)
        tracks = map (lambda track: (track.id
                                   , parser.parse(track.created_at))
                    , raw_tracks)

        recent_tracks.extend(tracks)

    recent_tracks.sort(key=lambda track: track[1])
    return recent_tracks