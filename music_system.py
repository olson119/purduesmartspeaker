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
        if (self.pointer > len(self.playlist) - 1):
            self.pointer = 0
        self.play()

    def prev_song(self):
        self.pointer -= 1
        if (self.pointer < 0):
            self.pointer = 0
        self.play()

     def quit(self):
         mixer.music.stop()
         mixer.quit()

    def check_busy(self):
        if (not mixer.music.get_busy() and not self.pause_flag ):
            if self.pointer > len(self.playlist) - 1:
            	self.ponter = 0
            	self.play()
            else:
                self.next_song()

    def run(self):
        self.play()
        print("Enter 'p' to pause, 'r' to resume, 'q' to skip, 'e' to go back, 'z' to quit ")
        while True:
            self.check_busy()

            if keyboard.is_pressed('p'):
                # Pausing the music
                self.pause()
                time.sleep(0.5)
            elif keyboard.is_pressed('r'):
                # Resuming the music
                self.unpause()
                time.sleep(0.5)
            elif keyboard.is_pressed('q'):
                self.next_song()
                time.sleep(0.5)
            elif keyboard.is_pressed('e'):
                self.prev_song()
                time.sleep(0.5)
            elif keyboard.is_pressed('z'):
                self.quit()
                break


if __name__ == "__main__":
    emotion = input("Please enter emotion: ")
    emotion = emotion.lower()
    playlist = create_playlist(emotion)
    system = MusicSystem(playlist)
    system.run()


