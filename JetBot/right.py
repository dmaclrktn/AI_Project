import cv2
import socket
import struct
import pickle
from jetbot import Robot, Camera
import time
import cv2
import random
import threading



    
    


# A¡ì¢¬¨­¢Òo ¨ù©øA¢´
robot = Robot()


while time.time() - start_time < 0.5:
    robot.set_motors(0.8, 0.8)
while time.time() - start_time < 1.5:
    robot.set_motors(0.65, 0.8)
while time.time() - start_time < 0.9:
    robot.set_motors(0.8, 0.8)
while time.time() - start_time < 1.5:
    robot.set_motors(0.8, 0.65)
while time.time() - start_time < 1:
    robot.set_motors(0.8, 0.8)