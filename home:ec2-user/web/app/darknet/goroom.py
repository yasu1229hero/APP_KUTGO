# Code written by Yasuhiro
# Transform into CLASS by Fitra
# Function    : to run the darknet app and count number of people from image taken
# Output      : number of people in a room
import subprocess
import os
import cv2
import datetime
import time
import scp

from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import shutil

class GoRoom:
    # initiate global variable
    number_of_people = 1
    command ='cd /home/ec2-user/web/app/darknet/ && /home/ec2-user/web/app/darknet/darknet detect cfg/yolov2.cfg /home/ec2-user/web/app/darknet/yolov2.weights room/test.jpg | grep person | wc -l'
    proc = ''
    t=''
    def __init__(self):
        # initiate private variable
        # self.HOST = '172.21.39.121'
        # self.PORT = "22"
        # self.USER = 'pi'
        # self.PSWD = '0000'

        # self.path1='/Users/yasu/darknet/'

        self.room_number='A309'
        self.stdout_data = ''
        self.stderr_data = ''

    def main_goroom(self):
        print('---------------detect object!------YOLOOOOOOhh!----------------')
        # run the command by subprocess
        GoRoom.proc = subprocess.Popen('cd /home/ec2-user/web/app/darknet/ && ~/web/app/darknet/darknet detect ~/web/app/darknet/cfg/yolov2.cfg yolov2.weights ~/web/app/darknet/room/roomA309.jpg | grep person | wc -l',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # os.system('cd /home/ec2-user/web/app/darknet/ && ~/web/app/darknet/darknet detect ~/web/app/darknet/cfg/yolov2.cfg yolov2.weights ~/web/app/darknet/room/test.jpg')
        #return value(stdout_data) is number of people
        self.stdout_data, self.stderr_data = GoRoom.proc.communicate()
        # print(self.stderr_data.decode('ascii'))
        print(self.stdout_data.decode('ascii'))
        #change the data type to int type
        GoRoom.number_of_people = int(self.stdout_data.decode('ascii'))
        #open the txt file to write room name and number of people
        print('-----------------There is ' + str(GoRoom.number_of_people) + ' people in the room '+self.room_number+'---------------')
        GoRoom.t=open('/home/ec2-user/web/app/darknet/count_people'+ self.room_number + '.txt','w')
        #write room name and number of people
        GoRoom.t.write('Number of people(' + self.room_number + ')' + '\n' +str(GoRoom.number_of_people))
        #print('There is ' + str(number_of_people) + ' people in the room A309')
        #wait 5min(300sec)
        print('---------------wait 2 minute------------------------------------')
        return GoRoom.number_of_people