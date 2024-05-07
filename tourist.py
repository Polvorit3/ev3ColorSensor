#!/usr/bin/env pybricks-micropython

# Client side code for 2 robots finding the border of a table problem.
# tourist.py
# Santiago de Chile 16/04/2024
# 
# Programmer: Matias Toledo, Rodrigo Cruz

from pybricks.hubs import EV3Brick
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

import urandom
import os

SPEED = 80
ev3 = EV3Brick()  # Initializes the Brick

#Get device name
with open('/etc/hostname') as hostname:
    myname = hostname.read()    #Name should be explorer
print(myname)

#Motor and other setups
left_motor = Motor(Port.D)  # left motor attached on port D 
right_motor = Motor(Port.A)  # right motor attached on port A
robot = DriveBase(left_motor, right_motor, wheel_diameter = 55, axle_track = 105)  # wheel_diameter = 52  axle_track= 125


SERVER = 'Explorer'
client = BluetoothMailboxClient()
movement_box = TextMailbox('movement', client)

print('waiting for connection...\n')
client.connect(SERVER)
print('Connected movement mailbox to Server\n')


movement_box.wait()
ev3.screen.print(movement_box.read())

message = movement_box.read()
array_message = message.split(",")
print(array_message, '\n')
print(len(array_message))

#Move robot
for i in range(len(array_message), 2):
    distance = int(array_message[i])
    angle = int(array_message[i + 1])

    robot.drive(SPEED, distance)
    robot.stop()  
    robot.straight(-100)
    robot.turn(angle)
    

