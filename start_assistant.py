from time import sleep

def Google_Assistant(q):
    #Start google assistant
    playMusic = 1 #if user says "Play music"
    q.put(playMusic)
