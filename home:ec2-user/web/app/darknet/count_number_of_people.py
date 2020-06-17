# Code written by Yasuhiro
# Function    : to run the darknet app and count number of people from image taken
# Output      : number of people in a room
import subprocess
import os
import subprocess
#import commands
import cv2
import datetime
import time
import scp

from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import shutil

#Yolov3

#export PATH="/home/pi/berryconda3/bin:$PATH"

def main():

    HOST = '172.21.39.121'
    PORT = "22"
    USER = 'pi'
    PSWD = '0000'

    path1='/Users/yasu/darknet/'

    room_number='A309'

    while True:


        print('---------------detect object!    ------YOLOOOOOOhh!----------------')

        command = './darknet detect cfg/yolov2.cfg yolov2.weights room/test.jpg | grep person | wc -l'
        proc = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        #return value(stdout_data) is number of people
        stdout_data, stderr_data = proc.communicate()
        #change the data type to int type
        number_of_people = int(stdout_data.decode('ascii'))
        #open the txt file to write room name and number of people
        print('-----------------There is ' + str(number_of_people) + ' people in the room A309---------------')
        t=open('/home/ec2-user/web/app/darknet/count_people'+ room_number + '.txt','w')
        #write room name and number of people
        t.write('Number of people(' + room_number + ')' + '\n' +str(number_of_people))
        #print('There is ' + str(number_of_people) + ' people in the room A309')
        #wait 5min(300sec)
        print('---------------wait 2 minute------------------------------------')
        time.sleep(120)

#you can delete this function
def camera():
    path1='/Users/man/SE/darknet/room_camera/'
    cap=cv2.VideoCapture(1)
    size = (800, 600)

    while True:
        ret,frame = cap.read()
        frame = cv2.resize(frame, size)

        now = datetime.datetime.now()
        mintime='{0:%M}'.format(now)
        mintime=int(mintime)
        min5 = mintime % 5

        print('----------------------------')

        if  min5 == 0:
                now = datetime.datetime.now()
                frname='t_{0:%m%d%H%M%S}.jpg'.format(now)
                cv2.imwrite( path1 + frname , frame)

#you can delete this function
def test():


    #scp pi@[172.21.39.116]:/home/pi/camera/A.jpg /Users/yasu

    HOST = '172.21.39.116'
    PORT = "22"
    USER = 'pi'
    PSWD = '0000'

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(HOST, port=PORT,username=USER, password=PSWD)

    scp = SCPClient(ssh.get_transport())
    scp.get('/home/pi/camera/roomA309.jpg')

    path1='/Users/yasu/darknet/'
    #copy roomA309.jpg to ./room
    shutil.copyfile(path1 + 'roomA309.jpg', path1 + '/room/roomA309.jpg')

    os.remove(path1 + 'roomA309.jpg')
    #print(new_path)

if __name__ == '__main__':
	main()
    #camera()
    #test()
