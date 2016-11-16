import argparse
import json
import urllib.parse
import urllib.request
import uuid


def rate(user_id, key, song_id):
    url = 'http://rainwave.cc/api4/rate'
    params = {'user_id': user_id, 'key': key, 'rating': 3, 'song_id': song_id,
              'sid': 2}
    data = urllib.parse.urlencode(params).encode()
    headers = {'user-agent': str(uuid.uuid4())}
    req = urllib.request.Request(url, data, headers)
    return urllib.request.urlopen(req)


def unrated_songs(user_id, key):
    url = 'http://rainwave.cc/api4/unrated_songs'
    params = {'user_id': user_id, 'key': key, 'sid': 2}
    data = urllib.parse.urlencode(params).encode()
    headers = {'user-agent': str(uuid.uuid4())}
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    body = response.read().decode()
    j = json.loads(body)
    for song in j['unrated_songs']:
        yield song


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_id')
    parser.add_argument('key')
    return parser.parse_args()


def main():
    args = parse_args()
    for song in unrated_songs(args.user_id, args.key):
        try:
            print('Attempting to rate {} // {}'.format(song['album_name'], song['title']))
        except UnicodeEncodeError:
            print('Attempting to rate song {}'.format(song['id']))
        rate(args.user_id, args.key, song['id'])

if __name__ == '__main__':
    main()
