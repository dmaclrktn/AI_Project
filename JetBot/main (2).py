import cv2
import socket
import struct
import pickle
from jetbot import Robot, Camera
import time
import cv2
import random



    
    


# A¡ì¢¬¨­¢Òo ¨ù©øA¢´
robot = Robot()

def right():
    print("right")
    print("right")
    print("right")
    print("right")
    print("right")
    print("right")
    print("right")
    print("right")
    
    start_time = time.time()
    while time.time() - start_time < 0.95:
        robot.set_motors(0.9, 0.75)
    start_time = time.time()
    while time.time() - start_time < 0.95:
        robot.set_motors(0.65, 0.95)
    #start_time = time.time()
    #if time.time() - start_time < 0.95:
    #    robot.set_motors(0.9, 0.75)
   # start_time = time.time()
   # if time.time() - start_time < 0.95:
    #    robot.set_motors(0.65, 0.95)
    #robot.set_motors(0.8, 0.8)
    #time.sleep(0.5)
    #robot.set_motors(0.9, 0.75)
    #time.sleep(0.95)
    #robot.set_motors(0.65, 0.95)
    #time.sleep(0.95)
    #robot.set_motors(0.8, 0.8)
    #time.sleep(0.5)
    #robot.stop()

def left():
    #robot.set_motors(0.8, 0.8)
    #time.sleep(0.5)
    print("left")
    print("left")
    print("left")
    print("left")
    print("left")
    print("left")
    print("left")
    print("left")

    start_time = time.time()
    while time.time() - start_time < 0.95:
        robot.set_motors(0.75, 1)
    start_time = time.time()
    while time.time() - start_time < 0.95:
        robot.set_motors(1, 0.75)


#cap = cv2.VideoCapture(gstreamer_pipeline(framerate=60), cv2.CAP_GSTREAMER)
#cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=320, height=240, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink', cv2.CAP_GSTREAMER)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
#cap = cv2.VideoCapture(create_gstreamer_pipeline(), cv2.CAP_GSTREAMER)
# ¨ùOAI ¨ù©øA¢´
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '141.223.140.40'  # ¢¯i¨¬¨¢Ao ¨ù¡©©öoAC IP AO¨ùO
port = 9918              # ¨ù¡©©öo¢¯I ¥ì¢¯AICN ¨¡¡À¨¡¢ç
SIZE = 12

client_socket.connect((host_ip, port))  # ¨ù¡©©öo¢¯¢® ¢¯¡þ¡Æa

while True:
    ret, frame = cap.read()  # A¡ì¢¬¨­¢Òo¡¤I¨¬IAI CA¡¤©öAO A¨¢¡¾a
    if ret:
        # CA¡¤©öAOA¡í ©öUAI¨¡¢ç¡¤I AIAU¥ìu
        #gpu_frame = cv2.cuda_GpuMat()
        #gpu_frame.upload(frame)
        data = pickle.dumps(frame)
        message_size = struct.pack("L", len(data))  # CA¡¤©öAO ¥ì¡ÍAIAIAC A¨Ï¡¾a ¨¡¨¢A¡ÆA¢®
        # ¥ì¡ÍAIAI Au¨ùU
        client_socket.sendall(message_size + data)
    if cv2.waitKey(10) == 13:  # Enter A¡Æ¢¬| ¢¥¨Ï¢¬¡Ì¢¬e A¨ú¡¤a
        break
    

    msg = client_socket.recv(SIZE)
    #msg = int.from_bytes(msg, "little")
    left_speed, right_speed ,decision= struct.unpack("fff",msg)

    print(left_speed, right_speed, decision)

    
    if decision == 4:
        robot.set_motors(left_speed, right_speed)
    elif decision == 3 or righting == 1:
        start_time = time.time()
        righting = right()
    elif decision == 1 and lefting == 1:
        start_time = time.time()
        lefting = left()
    else:
        robot.set_motors(left_speed, right_speed)
    #robot.set_motors(left_speed, right_speed)

    #robot.set_motors(left_speed, right_speed)
    #time.sleep(5.0)
    #robot.stop()
  
        

cap.release()
client_socket.close()

