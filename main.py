from camera import *
from generate_playlist import *
import time


### Facial Detection Code Block ###
start_time = time.time()
emotions = cameraMain()
print("Runtime = %s seconds" % (time.time()-start_time)) #measure runtime for testing
print(emotions) #print dictionary
most_freq_emotion = (max(emotions, key=emotions.get)) #return most frequently occurring emotion
print(most_freq_emotion)



### Music Playlist Code Block ###
emotion = most_freq_emotion
emotion = emotion.lower()
playlist = create_playlist(emotion)
print(len(playlist))
print(playlist)


### Music Playback Code Block ###

