# notes
* urls.py - routing, define urls here
* settings.py - get dependencies, define database
* basic workflow to get started: http://www.tangowithdjango.com/book17/chapters/setup.html#basic-workflows (define project then application then routes)

# ideas
* incorporate some kind of learning to determine what kind of songs a user actually likes, to choose the correct artists to show in the feed. 
* think of a better layout 
    - categorize by genre? order by how likely a user is to like a song?

# todo
1. parse all tracks that are reposted (https://api-v2.soundcloud.com/profile/soundcloud:users:41691970?limit=50&offset=0)
2. display these recent tracks sequentially on webpage

# depends
$ pip install soundcloud
$ pip install python-dateutil
