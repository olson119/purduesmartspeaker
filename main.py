from camera import *
from generate_playlist import *
from music_system import *
import time


### Facial Detection Code Block ###
start_time = time.time()
emotion = cameraMain()
print("Runtime = %s seconds" % (time.time()-start_time)) #measure runtime for testing
print("Playlist emotion: {}".format(emotion)) #print most frequent emotion


### Music Playlist Code Block ###
emotion = emotion.lower()
playlist = create_playlist(emotion)
print(len(playlist))
print(playlist)


### Music Playback Code Block ###
#system = MusicSystem(playlist)
#system.run()


from pygame import mixer
from generate_playlist import create_playlist
import keyboard
import time

music_folder = "/home/pi/Desktop/Face Detection/Music/SpotifyMusic/"

class MusicSystem:

    def __init__(self, playlist):
        self.playlist = [music_folder + i for i in playlist]
        mixer.init()
        self.pointer = 0
        self.pause_flag = False

    def play(self):
        mixer.music.load(self.playlist[self.pointer])
        mixer.music.play()

    def pause(self):
        mixer.music.pause()
        self.pause_flag = True

    def unpause(self):
        mixer.music.unpause()
        self.pause_flag = False

    def next_song(self):
        self.pointer += 1
        if (self.pointer > len(playlist)):
            self.pointer = 0
        self.play()

    def prev_song(self):
        self.pointer -= 1
        if (self.pointer < 0):
            self.pointer = 0
        self.play()

    # play next song when finished
    def check_busy(self):
        if (not mixer.music.get_busy() and not self.pause_flag ):
            self.next_song()

    def run(self):
        self.play()
        print("Enter 'p' to pause, 'r' to resume, 'q' to skip, 'e' to go back ")
        while True:
            self.check_busy()

            if keyboard.is_pressed('p'):
                # Pausing the music
                system.pause()
                time.sleep(0.5)
            elif keyboard.is_pressed('r'):
                # Resuming the music
                system.unpause()
                time.sleep(0.5)
            elif keyboard.is_pressed('q'):
                system.next_song()
                time.sleep(0.5)
            elif keyboard.is_pressed('e'):
                system.prev_song()
                time.sleep(0.5)



if __name__ == "__main__":
    system = MusicSystem(playlist)
    system.run()
