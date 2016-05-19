#coding=utf-8
#import player
from api import NetEase
import mp3play
import time

netease = NetEase()
data = netease.search(u'南山南', stype=1, offset=0, total='true', limit=60)
print data
song_ids = []
if 'songs' in data['result']:
    if 'mp3Url' in data['result']['songs']:
        songs = data['result']['songs']
        print songs
        
    else:
        for i in range(0, len(data['result']['songs']) ):
            song_ids.append( data['result']['songs'][i]['id'] )
        songs = netease.songs_detail(song_ids)
mp3_url_data = netease.dig_info(songs, 'songs') 
print mp3_url_data

for mp3_url  in mp3_url_data:
    print mp3_url['album_name']
    print mp3_url['artist']
    print mp3_url['song_name']
    print mp3_url['mp3_url']
    print '---------------------------'
#{'mp3_url': u'http://m2.music.126.net/GkFXC6qt6rEU2q9KYU-6yQ==/1373290025677371.mp3', 'song_id': 41462137, 'album_name': u'\u6587\u6b66\u8d1d\u94a2\u7434\u6539\u7f16\u4f5c\u54c1\u96c6\uff082015\u5e74\u5168\u96c6\uff09', 'song_name': u'\u5357\u5c71\u5357-\u6587\u6b66\u8d1d\u94a2\u7434\u7248', 'artist': u'\u6587\u6b66\u8d1d'}


