from generate_playlist import create_playlist
#!/usr/bin/python

import subprocess
subprocess.call("bash music_playback.sh", shell=True)

def convert_playlist_txt(playlist):
    for i in playlist:
        text_file = open("song.txt", "w", encoding='utf-8')
        print(i,file=text_file)
        text_file.close()

if __name__ == "__main__":
    emotion = input("Please enter emotion: ")
    emotion = emotion.lower()
    test = create_playlist(emotion)
    convert_playlist_txt(test)
    

