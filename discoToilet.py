# Disco Toilet v0.1
# Programming by Charlie Langridge
# charlie@charlielangridge.com

# Load Dependenciess
import pygame
import os
import time
from random import randint

# Bootstrap Code
pygame.mixer.init()

## TEMP CODE
global lightSwitch
lightSwitch = True

# Define Inputs and Outputs
# pullswitch = button(1)

# Functions

def discoBallOn():
    # Main Lights Off
    # Spot Light On
    # Mirror Ball On
    print("Disco On")

def discoBallOff():
    # Mirror Ball Off
    # Main Light On
    # Spot Light Off
    print("Disco Off")

def scanMusic():
    tracks = []
    for file in os.listdir("music"):
        if file.endswith(".mp3"):
            tracks.append(os.path.join(file))
    return tracks

def playRandomTrack(tracks):
    # Choose random number between 0 and X
    choice = randint(1,len(tracks))
    url = "music/" +tracks[choice-1]
    pygame.mixer.music.load(url)
    pygame.mixer.music.play(1)
    print ("PLAYING: " + tracks[choice-1])
    while (pygame.mixer.music.get_busy()):
        continue
    discoBallOff();

    
def menuLoop(tracks):
    menuKey = ""
    while True:
        _=os.system("clear")
        print ("##############################")
        print ("######## DISCO TOILET ########")
        print ("##############################")
        print ("###### "+str(len(tracks))+" TRACKS LOADED #######")
        print ("##############################")
        print ("# L = List Tracks            #")
        print ("# T = Trigger Sensor         #")
        print ("# X = Exit                   #")
        print ("##############################")
        if (lightSwitch):
            print ("# LIGHT SWITCH IS ON         #")
        else:
            print ("# LIGHT SWITCH IS OFF        #")
        print ("##############################")
            
        menuKey = input("Command: ")

        if (menuKey == "X") or (menuKey == "x"):
            break
        elif (menuKey == "L") or (menuKey == "l"):
            _=os.system("clear")
            print ("Files on system:")
            i = 1
            for file in os.listdir("music"):
                if file.endswith(".mp3"):
                    print(str(i) + ": " + os.path.join(file))
                    i = i + 1;
            input("Press Enter to continue...")

        elif (menuKey == "T") or (menuKey == "t"):
            _=os.system("clear")
            discoBallOn()
            playRandomTrack(tracks)
        
        continue
    

# Main Code
tracks = scanMusic()

menuLoop(tracks)
