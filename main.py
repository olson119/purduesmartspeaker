from camera import *
from generate_playlist import *
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

