from generate_playlist import *
from convert_playlist import *
from subprocess import call

def select_playlist(emotion):
    rc = call("./kill_music.sh")
    emotion = emotion.lower()
    playlist = create_playlist(emotion)
    try:
        convert_playlist_txt(playlist)
    except KeyboardInterrupt:
        print('Music playback stopped')