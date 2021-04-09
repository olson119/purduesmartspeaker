from generate_playlist import create_playlist
from subprocess import call

def convert_playlist_txt(playlist):
    for i in playlist:
        text_file = open("song.txt", "w", encoding='utf-8')
        print(i,file=text_file)
        text_file.close()
        rc = call("./music_playback.sh")

#if __name__ == "__main__":
#    emotion = input("Please enter emotion: ")
#    emotion = emotion.lower()
#    test = create_playlist(emotion)
#    convert_playlist_txt(test)
    

