from soundcloud_secret import *
from pprint import pprint
from datetime import timedelta, date
from dateutil import parser

import soundcloud

class Feed:
    def __init__(self, client, username):
        id = client.get('/resolve', url='http://soundcloud.com/%s/' % username).id
        count = client.get('users/%s/' % id).followings_count
        followings_raw = client.get('users/%s/followings' % id, limit=count)
        followings = map(lambda artist: artist.id, followings)
        self.feed = self.followings_recents()

        # todo build reposted tracks as well

    def followings_recents(self):
        recency = timedelta(days = 2)
        oldest = date.today() - recency
        oldest_fmtted = { 'from': '%u-%u-%u 00:00:00' % (oldest.year, oldest.month, oldest.day) }

        recent_tracks = []

        for artist in self.followings:
            raw_tracks = self.client.get('users/%s/tracks' % artist, created_at=oldest_fmtted)
            tracks = map (lambda track: (track.id
                                       , track.created_at)
                        , raw_tracks)

            recent_tracks.extend(tracks)

        recent_tracks.sort(key=lambda track: parser.parse(track[1]))
        return recent_tracks

def main():
    client = soundcloud.Client(client_id='58b4b27103ca13cfc7675ca4bb6f9a5d')
    me = Feed(client, 'fsxfreak')
    print me.feed

if __name__ == "__main__":
    main()
