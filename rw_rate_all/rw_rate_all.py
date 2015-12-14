import json
import os
import urllib.parse
import urllib.request


def rate(song_id):
    params = {'user_id': 3, 'key': os.environ['RW_KEY'], 'rating': 3,
              'song_id': song_id, 'sid': 2}
    data = urllib.parse.urlencode(params).encode()
    return urllib.request.urlopen('http://rainwave.cc/api4/rate', data)


def unrated_songs():
    params = {'user_id': 3, 'key': 'HzAFqoNe1u', 'sid': 2}
    data = urllib.parse.urlencode(params).encode()
    response = urllib.request.urlopen('http://rainwave.cc/api4/unrated_songs',
                                      data)
    body = response.read().decode()
    j = json.loads(body)
    for song in j['unrated_songs']:
        yield song


def main():
    for song in unrated_songs():
        print('rating {}'.format(song['title']))
        rate(song['id'])

if __name__ == '__main__':
    main()
