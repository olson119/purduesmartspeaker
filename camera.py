from picamera import PiCamera
from time import sleep
from deepface import DeepFace
from collections import defaultdict
import time #for tracking program runtime
import sys
import select
from subprocess import call
from queue import Queue
import threading
from start_assistant import *

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
    playMusic = 0
    iteration1 = 0
    #Camera Settings
    camera = PiCamera()
    camera.rotation = 180 #change depending on camera orientation
    camera.resolution = (256,256) #change resolution to increase quality vs decrease runtime
    filepath = "/home/pi/Desktop/Face Detection/Pictures"
    
    #Multithreading
    q = Queue()
    Google_thread = threading.Thread(target=Google_Assistant, args=(q, ))
    Google_thread.daemon = True
    Google_thread.start() 
    
    #Image Capturing and Emotion Detection
    dom_emotionDict = defaultdict(lambda:0) #emotion library
    while playMusic == 0: #take pictures until user asks to play music
        objs = takePicture(camera,filepath) #instructs camera to take picture
        emotionDict = objs["instance_1"]["emotion"] #dictionary of emotion weights
        print(emotionDict)
        playlists = ["happy", "sad", "angry", "neutral"]
        emotionDict = dict(map(lambda k: (k, emotionDict[k]), filter(lambda j: j in playlists, emotionDict))) #filter dictionary to only include emotions that have corresponding playlists        
        dom_emotion = max(emotionDict, key=emotionDict.get) #get dominant emotion
        print("Detected emotion: {}".format(dom_emotion))
        dom_emotionDict['{}'.format(dom_emotion)]+=1 #keep track of all dominant emotions over a time period
        
        if q.empty and (iteration1 == 1):
        #if q.empty:
            playMusic = q.get()
        print(playMusic)
        iteration1 = 1
    print("\nImage capturing stopped")
    most_freq_emotion = (max(dom_emotionDict, key=dom_emotionDict.get)) #return most frequently occuring dominant emotion
    return most_freq_emotion


#cameraMain()