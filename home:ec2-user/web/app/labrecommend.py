# Normal python code written by Kanji
# Transform into CLASS by Fitra
# Function    : to find the recommended lab based on the lab data and input by user
# Output      : lab recommendation data

import csv
import pandas as pd
import sys
import io

class LabRecommend:
	# initiate the public variable
	room_data = []
	lab_data = []
	def __init__(self):
		# initiate the private variable
		self.csv_input = ''
		self.keyword = ''
		self.content = ''
		self.input_line = []
		self.csv_input2 = ''
		self.r = ''
		self.recommend_lab = []
	def main_lab(self):	
		# read the labdata and keyword files. 
		self.csv_input = pd.read_csv(filepath_or_buffer="/home/ec2-user/web/app/labdata.csv", encoding="ms932", sep=",")
		self.keyword = io.open("/home/ec2-user/web/app/keyword.txt", "r", encoding="utf8")

		# Save into the content and input_line variable
		self.content = self.keyword.readlines()
		for i in range(len(self.content)):
			self.content[i] = self.content[i].strip()
		
		self.input_line = []
		for k in range(24):
			self.input_line.append('null')
		for h in range(len(self.content)):
			self.input_line[h] = self.content[h]

		# close the io open
		# print(self.content)
		# print(self.input_line)
		self.keyword.close()

		# compare the input keyword with the lab data file. If the same keyword inside the lab data file, put everything into the csv_input2
		self.csv_input2 = self.csv_input[(self.csv_input["keyword1"] == self.input_line[0]) | (self.csv_input["keyword1"] == self.input_line[1]) | (self.csv_input["keyword1"] == self.input_line[2]) 
		| (self.csv_input["keyword1"] == self.input_line[3]) | (self.csv_input["keyword1"] == self.input_line[4]) | (self.csv_input["keyword1"] == self.input_line[5])
		| (self.csv_input["keyword1"] == self.input_line[6]) | (self.csv_input["keyword1"] == self.input_line[7]) | (self.csv_input["keyword1"] == self.input_line[8])
		| (self.csv_input["keyword1"] == self.input_line[9]) | (self.csv_input["keyword1"] == self.input_line[10]) | (self.csv_input["keyword1"] == self.input_line[11])
		| (self.csv_input["keyword1"] == self.input_line[12]) | (self.csv_input["keyword1"] == self.input_line[13]) | (self.csv_input["keyword1"] == self.input_line[14])
		| (self.csv_input["keyword1"] == self.input_line[15]) | (self.csv_input["keyword1"] == self.input_line[16]) | (self.csv_input["keyword1"] == self.input_line[17])
		| (self.csv_input["keyword2"] == self.input_line[0]) | (self.csv_input["keyword2"] == self.input_line[1]) | (self.csv_input["keyword2"] == self.input_line[2]) 
		| (self.csv_input["keyword2"] == self.input_line[3]) | (self.csv_input["keyword2"] == self.input_line[4]) | (self.csv_input["keyword2"] == self.input_line[5])
		| (self.csv_input["keyword2"] == self.input_line[6]) | (self.csv_input["keyword2"] == self.input_line[7]) | (self.csv_input["keyword2"] == self.input_line[8])
		| (self.csv_input["keyword2"] == self.input_line[9]) | (self.csv_input["keyword2"] == self.input_line[10]) | (self.csv_input["keyword2"] == self.input_line[11])
		| (self.csv_input["keyword2"] == self.input_line[12]) | (self.csv_input["keyword2"] == self.input_line[13]) | (self.csv_input["keyword2"] == self.input_line[14])
		| (self.csv_input["keyword2"] == self.input_line[15]) | (self.csv_input["keyword2"] == self.input_line[16]) | (self.csv_input["keyword2"] == self.input_line[17])
		| (self.csv_input["keyword3"] == self.input_line[0]) | (self.csv_input["keyword3"] == self.input_line[1]) | (self.csv_input["keyword3"] == self.input_line[2]) 
		| (self.csv_input["keyword3"] == self.input_line[3]) | (self.csv_input["keyword3"] == self.input_line[4]) | (self.csv_input["keyword3"] == self.input_line[5])
		| (self.csv_input["keyword3"] == self.input_line[6]) | (self.csv_input["keyword3"] == self.input_line[7]) | (self.csv_input["keyword3"] == self.input_line[8])
		| (self.csv_input["keyword3"] == self.input_line[9]) | (self.csv_input["keyword3"] == self.input_line[10]) | (self.csv_input["keyword3"] == self.input_line[11])
		| (self.csv_input["keyword3"] == self.input_line[12]) | (self.csv_input["keyword3"] == self.input_line[13]) | (self.csv_input["keyword3"] == self.input_line[14])
		| (self.csv_input["keyword3"] == self.input_line[15]) | (self.csv_input["keyword3"] == self.input_line[16]) | (self.csv_input["keyword3"] == self.input_line[17])]
		# print(self.csv_input2)

		# write all the csv_input2 into the recommend.csv file
		self.csv_input2.to_csv("/home/ec2-user/web/app/recommend.csv",encoding="utf_8_sig")

		self.r = csv.reader(open('/home/ec2-user/web/app/recommend.csv'))
		self.recommend_lab = list(self.r)
		
		# put the result of room data and lab data to variable
		LabRecommend.room_data = [self.recommend_lab[i][2] for i in range(len(self.recommend_lab))]
		LabRecommend.lab_data = [self.recommend_lab[i][3] for i in range(len(self.recommend_lab))]

		# return the output of the function
		return LabRecommend.room_data, LabRecommend.lab_data