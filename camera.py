from picamera import PiCamera
from time import sleep
from deepface import DeepFace
from collections import defaultdict
import time #for tracking program runtime

## for removing tf warnings
import logging
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)


#take picture and send it to be analyzed
def takePicture(camera,filepath):
    objs = 0
    #camera.start_preview()
    while objs == 0:
        sleep(0.1)
        print('click')
        camera.capture('{}/image0.jpg'.format(filepath))
        objs = analyze(camera,filepath)
    #camera.stop_preview()
    return objs

#analyze 10 pictures and put emotions into dict, pick the most common emotion
def analyze(camera,filepath):
    try:
        objs = DeepFace.analyze(["%s/image0.jpg"% filepath], actions = ['emotion'])
    except ValueError as e:
        print('No face detected')
        picture = 0
        return picture
    print('Face acquired')
    return objs


def cameraMain():
    camera = PiCamera()
    camera.rotation = 180 #change depending on camera orientation
    camera.resolution = (64,64) #change resolution to increase quality vs decrease runtime
    filepath = "/home/pi/Desktop/Face Detection/Pictures"
    #playMusic = 0
    emotions = defaultdict(lambda:0) #emotion library
    try:
        while True: #take pictures until user asks to play music
            objs = takePicture(camera,filepath)
            #playMusic += 1 #would be controlled by google assistant
            print(objs)
            #print(objs["instance_1"]["dominant_emotion"])
            emotions['{}'.format(objs["instance_1"]["dominant_emotion"])]+=1
    except KeyboardInterrupt:
        print("\nImage capturing stopped")
    return emotions


#start_time = time.time()
#emotions = main()

#print("Runtime = %s seconds" % (time.time()-start_time)) #measure runtime for testing
#print(emotions) #print dictionary
#most_freq_emotion = (max(emotions, key=emotions.get)) #return most frequently occurring emotion
#print(most_freq_emotion)


