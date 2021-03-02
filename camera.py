from picamera import PiCamera
from time import sleep
from deepface import DeepFace
camera = PiCamera()
camera.rotation = 180 #change depending on camera orientation

camera.start_preview()
for i in range (3): #change to while loop that takes pictures until receives signal from google assistant
    sleep(3)
    camera.capture('/home/pi/Desktop/Face Detection/Pictures/image%s.jpg' % i)
    
    #camera.start_recording('/home/pi/Desktop/video.h264')
    #sleep(5) #record 5 seconds of video
    #camera.stop_recording()
camera.stop_preview()

#DeepFace.stream("/home/pi/Desktop/video.h264")

#analyze 10 pictures and put emotions into dict, pick the most common emotion
obj = DeepFace.analyze(img_path="/home/pi/Desktop/image0.jpg", actions = ['emotion'])
#objs = DeepFace.analyze(["image1.jpg","image2.jpg"])
print(obj["dominant_emotion"])
#print(objs["dominant_emotion"])