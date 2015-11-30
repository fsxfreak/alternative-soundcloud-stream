from soundcloud_secret import *
from pprint import pprint
from datetime import timedelta, date, datetime
from dateutil import parser
import json
import soundcloud

# for undocumented api
import urllib2

def oldest_date(days_ago):
    recency = timedelta(days = days_ago)
    oldest = date.today() - recency
    oldest_fmtted = { 'from': '%u-%u-%u 00:00:00' % (oldest.year, oldest.month, oldest.day) }

    return oldest_fmtted

def oldest_date_raw(days_ago):
    oldest_date_json = oldest_date(days_ago)
    return ' '.join(oldest_date_json['from'].split()[:1])

def build_feed(username, track_days_ago, repost_days_ago):
    client = soundcloud.Client(client_id='58b4b27103ca13cfc7675ca4bb6f9a5d')

    id = client.get('/resolve', url='http://soundcloud.com/%s/' % username).id
    count = client.get('users/%s/' % id).followings_count
    followings_raw = client.get('users/%s/followings' % id, limit=count)
    followings = map(lambda artist: artist.id, followings_raw)

    oldest_fmtted = oldest_date(track_days_ago)
    oldest_repost = oldest_date_raw(repost_days_ago)

    recent_tracks = []

    for artist in followings:
        raw_tracks = client.get('users/%s/tracks' % artist, created_at=oldest_fmtted)

        tracks = map (lambda track: (track.id
                                   , str(datetime.strptime(
                                        track.created_at
                                      , '%Y/%m/%d %H:%M:%S +0000'))
                                   , track.title
                                   , track.user['username']
                                   , track.permalink_url
                                   , track.artwork_url)
                    , raw_tracks)

        recent_tracks.extend(tracks)
        reposts = build_reposts(artist, oldest_repost)
        recent_tracks.extend(reposts)

    for track in recent_tracks:
        print track

    return recent_tracks

def build_reposts(artist_id, oldest):
    limit = 10
    req_url = (
        'https://api-v2.soundcloud.com/profile/'
        'soundcloud:users:%d?limit=%d'
        ) % (artist_id, limit)

    parsed = json.loads(urllib2.urlopen(req_url).read())
    tracks_info = parsed['collection']

    reposts = []
    for track_info in tracks_info:
        if 'track' not in track_info:
            continue

        if track_info['type'] == 'track-repost':
            reposts.append(track_info)

    reposts_processed = map (lambda repost: ( repost['track']['id']
                                            , str(
                                                datetime.strptime(
                                                  repost['created_at']
                                                , '%Y-%m-%dT%H:%M:%SZ'))
                                            , repost['track']['title']
                                            , repost['track']['user']['username']
                                            , repost['track']['permalink_url']
                                            , repost['track']['artwork_url']
                                            )
                           , reposts)

    reposts_processed = filter(
               lambda repost: datetime.strptime(repost[1], '%Y-%m-%d %H:%M:%S') 
                            > datetime.strptime(oldest, '%Y-%m-%d')
             , reposts_processed)

    return reposts_processed

def main():
    # build_reposts(4061813, oldest_date_raw(5))
    build_feed('fsxfreak', 5, 3)

if __name__ == "__main__":
    main()

