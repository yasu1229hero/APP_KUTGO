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

        print('------------conect to raspberryPi and get room images----------')

        #setting of SSH
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(HOST, port=PORT,username=USER, password=PSWD)
        #SCP(download the room image from raspberry pi)
        scp = SCPClient(ssh.get_transport())
        scp.get('/home/pi/camera/roomA309.jpg')
        #change place to detect object by Yolov3
        shutil.copyfile(path1 + 'roomA309.jpg', path1 + '/room/roomA309.jpg')

        #なくてもよい(you can delete this code)
        os.remove(path1 + 'roomA309.jpg')

        print('---------------detect object!------YOLOOOOOOhh!----------------')

        #command to use yolov3          |grep person| wc -l  ←←　count(extract?) number of people in the all objects!
        command = './darknet detect cfg/yolov3.cfg yolov3.weights room/roomA309.jpg | grep person | wc -l'
        proc = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #return value(stdout_data) is number of people
        stdout_data, stderr_data = proc.communicate()
        #change the data type to int type
        number_of_people = int(stdout_data.decode('ascii'))
        #open the txt file to write room name and number of people
        t=open('/Users/yasu/darknet/count_people/'+ room_number + '.txt','w')
        #write room name and number of people
        t.write('Number of people(' + room_number + ')' + '\n' +str(number_of_people))
        print('There is ' + str(number_of_people) + ' people in the room A309')
        #wait 5min(300sec)
        time.sleep(120)

#you can delete this function
def camera():
    path1='/Users/man/SE/darknet/room_camera/'
    cap=cv2.VideoCapture(1)
    size = (800, 600)

    while True:
        ret,frame = cap.read()
        #サイスを変更
        frame = cv2.resize(frame, size)

        now = datetime.datetime.now()
        #分数を取得する(この時点では文字列型)
        mintime='{0:%M}'.format(now)
        #整数型に変換
        mintime=int(mintime)
        #5の倍数を取得(5分おき)
        min5 = mintime % 5

        print('----------------------------')

        if  min5 == 0:
                #時間取得
                now = datetime.datetime.now()
                #保存名を時間から設定
                frname='t_{0:%m%d%H%M%S}.jpg'.format(now)
                #第二引数はframeかdstを入れる
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

    #なくてもよい
    os.remove(path1 + 'roomA309.jpg')
    #print(new_path)

if __name__ == '__main__':
	main()
    #camera()
    #test()
