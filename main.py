from camera import *
import time


### Facial Detection Code Block ###
start_time = time.time()
emotions = cameraMain()
print("Runtime = %s seconds" % (time.time()-start_time)) #measure runtime for testing
print(emotions) #print dictionary
most_freq_emotion = (max(emotions, key=emotions.get)) #return most frequently occurring emotion
print(most_freq_emotion)




### Music Playback Code Block ###
