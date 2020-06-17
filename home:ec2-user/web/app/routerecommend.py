# Code written by Noda
# Transform into CLASS by Fitra
# Function    : to find the best route based on the keyword and priority
# Output      : list of buildings
# -*- coding: utf-8 -*-

import csv
import math
import io
from operator import itemgetter


class RouteRecommend:
    # initiate the private variables
    def __init__(self):
        self.keyword = ''
        self.chosenKeyword = []
        self.akey = ''
        self.Awing_key = []
        self.bkey = ''
        self.B_Cwing_key = []
        self.kkey = ''
        self.K_key = []
        self.centkey = ''
        self.CentralBuilding = []
        self.caffe = ''
        self.Caffe = []
        self.audito = ''
        self.Auditorium = []
        self.Awing_count=0
        self.B_Cwing_count=0
        self.K_count=0
        self.CentralBuilding_count=0
        self.Caffe_count=0
        self.Auditorium_count=0
        self.KeyWeight = []
        self.name_array1=[]
        self.name_array2=[]
        self.f = ''
        self.writer = ''
        self.aw = ''
        self.bc = ''
        self.kw = ''
        self.ce = ''
        self.cf = ''
        self.au = ''
    def main_route(self):
        # read the keyword
        self.keyword = io.open("/home/ec2-user/web/app/keyword.txt", "r", encoding="utf8")

        self.chosenKeyword = self.keyword.readlines()
        for i in range(len(self.chosenKeyword)):
            self.chosenKeyword[i] = self.chosenKeyword[i].strip()
        # read all the options keywords for each building data
        self.akey = io.open("/home/ec2-user/web/app/awing.txt", "r", encoding="utf8")
        self.Awing_key = self.akey.readlines()
        for j in range(len(self.Awing_key)):
            self.Awing_key[i] = self.Awing_key[i].strip()

        self.bkey = io.open("/home/ec2-user/web/app/bwing.txt", "r", encoding="utf8")
        self.B_Cwing_key = self.bkey.readlines()
        for b in range(len(self.B_Cwing_key)):
            self.B_Cwing_key[b] = self.B_Cwing_key[b].strip()

        self.kkey = io.open("/home/ec2-user/web/app/kkey.txt", "r", encoding="utf8")
        self.K_key = self.kkey.readlines()
        for k in range(len(self.K_key)):
            self.K_key[k] = self.K_key[k].strip()

        self.centkey = io.open("/home/ec2-user/web/app/CentralBuilding.txt", "r", encoding="utf8")
        self.CentralBuilding = self.centkey.readlines()
        for c in range(len(self.CentralBuilding)):
            self.CentralBuilding[c] = self.CentralBuilding[c].strip()

        self.caffe = io.open("/home/ec2-user/web/app/Caffe.txt", "r", encoding="utf8")
        self.Caffe = self.caffe.readlines()
        for ca in range(len(self.Caffe)):
            self.Caffe[ca] = self.Caffe[ca].strip()

        self.audito = io.open("/home/ec2-user/web/app/Auditorium.txt", "r", encoding="utf8")
        self.Auditorium = self.audito.readlines()
        for au in range(len(self.Auditorium)):
            self.Auditorium[au] = self.Auditorium[au].strip()

        # initiate the variables
        self.Awing_count=0
        self.B_Cwing_count=0
        self.K_count=0
        self.CentralBuilding_count=0
        self.Caffe_count=0
        self.Auditorium_count=0

        # count the number of keyword for each building
        for element in self.chosenKeyword:
            if element in self.Awing_key:
                self.Awing_count+=1
            elif element in self.B_Cwing_key:
                self.B_Cwing_count+=1
            elif element in self.CentralBuilding:
                self.CentralBuilding_count+=1
            elif element in self.Caffe:
                self.Caffe_count+=1
            elif element in self.Auditorium:
                self.Auditorium_count+=1
            elif element in self.K_key:
                self.K_count+=1
        self.KeyWeight=[[self.Awing_count,'Awing'], [self.B_Cwing_count, 'B_Cwing'], [self.K_count, 'K'], [self.CentralBuilding_count, 'CentralBuilding'], [self.Caffe_count, 'Caffe'], [self.Auditorium_count, 'Auditorium']]
        # safe all the weight of bulding into KeyWeight
        self.aw = self.KeyWeight[0]
        self.bc = self.KeyWeight[1]
        self.kw = self.KeyWeight[2]
        self.ce = self.KeyWeight[3]
        self.cf = self.KeyWeight[4]
        self.au = self.KeyWeight[5]
        self.KeyWeight.reverse()
        self.KeyWeight.sort(key=itemgetter(0))
        self.KeyWeight.reverse()

        # Make the route from the highest weight to the lowest weight
        if self.KeyWeight[0][1]=='Awing' and self.KeyWeight[1][1]=='B_Cwing':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.ce,self.kw,self.cf,self.au]
        elif self.KeyWeight[0][1]=='Awing' and self.KeyWeight[1][1]=='K':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.bc,self.ce,self.cf,self.au]
        elif self.KeyWeight[0][1]=='Awing' and self.KeyWeight[1][1]=='CentralBuilding':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.bc,self.kw,self.cf,self.au]
        elif self.KeyWeight[0][1]=='Awing' and self.KeyWeight[1][1]=='Caffe':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.bc,self.ce,self.cf,self.au]
        elif self.KeyWeight[0][1]=='Awing' and self.KeyWeight[1][1]=='Auditorium':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.cf,self.kw,self.ce,self.bc]
        elif self.KeyWeight[0][1]=='B_Cwing' and self.KeyWeight[1][1]=='K':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.cf,self.au,self.ce,self.aw]
        elif self.KeyWeight[0][1]=='B_Cwing' and self.KeyWeight[1][1]=='CentralBuilding':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.aw,self.kw,self.cf,self.au]
        elif self.KeyWeight[0][1]=='B_Cwing' and self.KeyWeight[1][1]=='Caffe':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.kw,self.ce,self.aw,self.au]
        elif self.KeyWeight[0][1]=='B_Cwing' and self.KeyWeight[1][1]=='Auditorium':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.cf,self.kw,self.ce,self.aw]
        elif self.KeyWeight[0][1]=='K' and self.KeyWeight[1][1]=='CentralBuilding':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.aw,self.bc,self.cf,self.au]
        elif self.KeyWeight[0][1]=='K' and self.KeyWeight[1][1]=='Caffe':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.au,self.ce,self.aw,self.bc]
        elif self.KeyWeight[0][1]=='K' and self.KeyWeight[1][1]=='Auditorium':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.cf,self.ce,self.aw,self.bc]
        elif self.KeyWeight[0][1]=='CentralBuilding' and self.KeyWeight[1][1]=='Caffe':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.au,self.kw,self.aw,self.bc]
        elif self.KeyWeight[0][1]=='CentralBuilding' and self.KeyWeight[1][1]=='Auditorium':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.cf,self.kw,self.aw,self.bc]
        elif self.KeyWeight[0][1]=='Caffe' and self.KeyWeight[1][1]=='Auditorium':
            self.KeyWeight=[self.KeyWeight[0],self.KeyWeight[1],self.kw,self.ce,self.aw,self.bc]
        elif self.KeyWeight[0][1]=='B_Cwing' and self.KeyWeight[1][1]=='Awing':
            self.KeyWeight=[self.aw,self.bw,self.kw,self.ce,self.cf,self.au]
        elif self.KeyWeight[0][1]=='K' and self.KeyWeight[1][1]=='Awing':
            self.KeyWeight=[self.aw,self.bd,self.kw,self.ce,self.cf,self.au]
        elif self.KeyWeight[0]=='CentralBuilding' and self.KeyWeight[1]=='Awing':
            self.KeyWeight=[self.ce,self.aw,self.bc,self.kw,self.cf,self.au]
        elif self.KeyWeight[0]=='Caffe' and self.KeyWeight[1]=='Awing':
            self.KeyWeight=[self.cf,self.ce,self.aw,self.bc,self.kw,self.au]
        elif self.KeyWeight[0]=='Auditorium' and self.KeyWeight[1]=='Awing':
            self.KeyWeight=[self.au,self.aw,self.bc,self.ce,self.kw,self.cf]
        elif self.KeyWeight[0]=='K' and self.KeyWeight[1]=='B_Cwing':
            self.KeyWeight=[self.kw,self.bc,self.aw,self.ce,self.cf,self.au]
        elif self.KeyWeight[0]=='CentralBuilding' and self.KeyWeight[1]=='B_Cwing':
            self.KeyWeight=[self.ce,self.aw,self.bc,self.kw,self.cf,self.au]
        elif self.KeyWeight[0]=='Caffe' and self.KeyWeight[1]=='B_Cwing':
            self.KeyWeight=[self.cf,self.kw,self.bc,self.aw,self.ce,self.au]
        elif self.KeyWeight[0]=='Auditorium' and self.KeyWeight[1]=='B_Cwing':
            self.KeyWeight=[self.au,self.cf,self.kw,self.bc,self.aw,self.ce]
        elif self.KeyWeight[0]=='CentralBuilding' and self.KeyWeight[1]=='K':
            self.KeyWeight=[self.ce,self.kw,self.cf,self.au,self.aw,self.bc]
        elif self.KeyWeight[0]=='Caffe' and self.KeyWeight[1]=='K':
            self.KeyWeight=[self.cf,self.kw,self.ce,self.aw,self.bc,self.au]
        elif self.KeyWeight[0]=='Auditorium' and self.KeyWeight[1]=='K':
            self.KeyWeight=[self.au,self.cf,self.kw,self.bc,self.aw,self.ce]
        elif self.KeyWeight[0]=='Caffe' and self.KeyWeight[1]=='CentralBuilding':
            self.KeyWeight=[self.cf,self.ce,self.aw,self.bc,self.kw,self.au]
        elif self.KeyWeight[0]=='Auditorium' and self.KeyWeight[1]=='CentralBuilding':
            self.KeyWeight=[self.au,self.cf,self.kw,self.ce,self.aw,self.bc]
        elif self.KeyWeight[0]=='Auditorium' and self.KeyWeight[1]=='Caffe':
            self.KeyWeight=[self.au,self.cf,self.kw,self.ce,self.aw,self.bc]

        # safe the weight into name_array1
        self.name_array1 = []
        for k in self.KeyWeight:
            self.name_array1.append(k)
        
        # safe the weight into name_array2
        self.name_array2 = []
        for j in self.name_array1:
            self.name_array2.append(j[1])

        # write the route result into the csv file
        self.f = open('/home/ec2-user/web/app/route.csv', 'w')
        self.writer = csv.writer(self.f, lineterminator='\n')
        self.writer.writerow(self.name_array2)
        self.f.close()

        # return the output of best route
        return self.name_array2
