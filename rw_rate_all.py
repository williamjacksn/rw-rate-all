import argparse
import json
import urllib.parse
import urllib.request
import uuid


def rate(user_id, key, song_id):
    url = 'https://rainwave.cc/api4/rate'
    params = {'key': key, 'rating': 3, 'sid': 2, 'song_id': song_id, 'user_id': user_id}
    data = urllib.parse.urlencode(params).encode()
    headers = {'user-agent': str(uuid.uuid4())}
    req = urllib.request.Request(url, data, headers)
    return urllib.request.urlopen(req)


def unrated_songs(user_id, key):
    url = 'https://rainwave.cc/api4/unrated_songs'
    params = {'key': key, 'sid': 2, 'user_id': user_id}
    data = urllib.parse.urlencode(params).encode()
    headers = {'user-agent': str(uuid.uuid4())}
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    body = response.read().decode()
    j = json.loads(body)
    for song in j.get('unrated_songs'):
        yield song


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interactive', action='store_true')
    parser.add_argument('user_id')
    parser.add_argument('key')
    return parser.parse_args()


def main():
    args = parse_args()
    for song in unrated_songs(args.user_id, args.key):
        album = song.get('album_name')
        title = song.get('title')
        song_id = song.get('id')
        try:
            print(f'Attempting to rate {album} // {title}')
        except UnicodeEncodeError:
            print(f'Attempting to rate song {song_id}')
        rate(args.user_id, args.key, song_id)
    if args.interactive:
        input('Press <Enter> ...')


if __name__ == '__main__':
    main()
