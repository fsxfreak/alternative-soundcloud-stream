from soundcloud_secret import *
from pprint import pprint
import soundcloud

class Follower:
	def __init__(self, client, username):
		self.id = client.get('/resolve', url='http://soundcloud.com/%s/' % username).id
		self.count = client.get('users/%s/followings_count' % id).followings_count
		followings = client.get('users/%s/followings' % id, limit=self.count)
		self.followings = map(lambda artist: artist.id, followings)


def followings(client, userid, followings_count):
	request = "/users/%s/followings" % userid;
	return client.get(request, limit=followings_count)

def id(client, username):
	url = "http://soundcloud.com/%s/" % username;
	return client.get('/resolve', url=url).id

def main():
	client = soundcloud.Client(client_id='58b4b27103ca13cfc7675ca4bb6f9a5d')
	me = Follower(client, 'fsxfreak')
	print(me.followings)

if __name__ == "__main__":
    main()
