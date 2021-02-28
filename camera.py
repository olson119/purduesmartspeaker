from picamera import PiCamera
from time import sleep
from deepface import DeepFace
camera = PiCamera()
camera.rotation = 180

camera.start_preview()
for i in range (3):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    
camera.stop_preview()

obj = DeepFace.analyze(img_path="/home/pi/Desktop/image0.jpg", actions = ['emotion'])
print(obj["dominant_emotion"])