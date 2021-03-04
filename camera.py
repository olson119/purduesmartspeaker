from picamera import PiCamera
from time import sleep
from deepface import DeepFace

def takePicture(camera,filepath):
    objs = 0
    camera.start_preview()
    while objs == 0:
        sleep(3)
        print('click')
        camera.capture('{}/image0.jpg'.format(filepath))
        objs = analyze(camera,filepath)
    return objs
    camera.stop_preview()

    #for i in range (1): #change to while loop that takes pictures until receives signal from google assistant
    #    sleep(3)
    #    camera.capture('{}/image{}.jpg'.format(filepath,i))
    #camera.stop_preview()
    #objs = analyze(camera,filepath)
    #return objs

#analyze 10 pictures and put emotions into dict, pick the most common emotion
def analyze(camera,filepath):
    try:
        objs = DeepFace.analyze(["%s/image0.jpg"% filepath], actions = ['emotion'])
        #objs = DeepFace.analyze(["%s/image0.jpg"% filepath,"%s/image1.jpg"% filepath,"%s/image2.jpg"% filepath], actions = ['emotion'])
    except ValueError as e:
        print('No face detected')
        picture = 0
        return picture
    print('Face acquired')
    return objs


def main():
    camera = PiCamera()
    camera.rotation = 180 #change depending on camera orientation
    filepath = "/home/pi/Desktop/Face Detection/Pictures"
    playMusic = 0
    while playMusic == 0: #take pictures until user asks to play music
        objs = takePicture(camera,filepath)
        #objs = analyze(camera,filepath)
        playMusic = 1 #would be controlled by google assistant
        #print(objs["instance_1"]["dominant_emotion"])
        print(objs)
main()

