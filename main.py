from camera import *
from generate_playlist import *
from convert_playlist import *
import time
from subprocess import call


### Facial Detection Code Block ###
start_time = time.time()
emotion = cameraMain()
print("Runtime = %s seconds" % (time.time()-start_time)) #measure runtime for testing
print("Playlist emotion: {}".format(emotion)) #print most frequent emotion


### Music Playlist Code Block ###
emotion = emotion.lower()
playlist = create_playlist(emotion)

### Music Playback Code Block ###
try:
    convert_playlist_txt(playlist)
except KeyboardInterrupt:
    print('Music playback stopped')


    


