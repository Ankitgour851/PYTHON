from pygame import init, mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")


if __name__=='__main__':
    # musiconloop("Hamein Tumse Hua Pyar.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=15
    exsecs=30
    eyesecs=60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time.Enter 'Drank' to stop")
            musiconloop("Hamein Tumse Hua Pyar.mp3","Drank")
            init_water=time()
            log_now("Drank water at")

        if time() - init_exercise > exsecs:
            print("Physical exercise time.Enter 'Physical' to stop")
            musiconloop("Hamein Tumse Hua Pyar.mp3","Physical")
            init_exercise=time()
            log_now("Physical Exercise at")

        if time() - init_eyes > eyesecs:
            print("Eye excercise time.Enter 'Eye' to stop")
            musiconloop("Hamein Tumse Hua Pyar.mp3","Eye")
            init_eyes=time()
            log_now("Eye Exercise at")
            