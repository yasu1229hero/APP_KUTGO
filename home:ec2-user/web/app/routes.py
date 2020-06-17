# Code written by Fitra
# Function    : to make the route of the website
# Output      : route of every pages
from app import app
from flask import Flask, render_template, flash, redirect, request, url_for, send_from_directory
from app.darknet.goroom import GoRoom
from app.keywordsform import KeywordsForm
from app.labrecommend import LabRecommend
from app.routerecommend import RouteRecommend
import time
import io
import pandas as pd
import unicodecsv as csv
import json
from io import open

# get config and give SECRETKEY
app.config.from_object(__name__)
app.config['SECRETKEY']='65a6b5e4a3204bdd87adb7b1a98eafaa'

# initiate global variable
goroom_class = None
labr_class = None
route_class = None
number_of_people = 0

# render the index page
@app.route('/')
@app.route('/index')
def index():
    return render_template('counthome.html')

# make a link for room image to be accessed in html
@app.route('/uploads/<path:filename>')
def download_file(filename):
	return send_from_directory('/home/ec2-user/web/app/darknet/room/',filename, as_attachment=True)

# render the buildinga page
@app.route('/buildinga')
def buildinga():
	# take the global variable
	global goroom_class
	global number_of_people

	# construct the class
	if goroom_class == None:
		goroom_class = GoRoom()

	# run the main function
	number_of_people = goroom_class.main_goroom()

	# return render_template('buildinga.html')
	return render_template('buildinga.html',nop=number_of_people)

# render the gochat page
@app.route('/gochat')
def gochat():
	return render_template('chatbothome.html')

# render the schedulehome page
@app.route('/goschedule', methods=['GET', 'POST'])
def goschedule():
	# form = KeywordsForm()
	# if request.method == 'POST':
	# 	result = request.form
	# 	print(result)
	# 	print(result.get('data'))
	# 	return redirect(url_for('confirmationroute',data = result.get('data')))
	return render_template('schedulehome.html')

# render confirmationroute page
@app.route('/confirmationroute', methods=['GET', 'POST'])
def confirmationroute():
	# get the form data using post
	if request.method == 'POST':
		data = request.form
		# write the keyword data into keyword.txt file
		with open('/home/ec2-user/web/app/keyword.txt', 'w', encoding='utf-8') as f:
			for key, value in data.items():
				f.write(value + "\n")
		return render_template("confirmationkeywords.html",data = data)
	return render_template('confirmationkeywords.html', data=data)

# render the recommendedroute page	
@app.route('/recommendedroute')
def recommendedroute():
	# global goroom_class
	# global number_of_people

	# take the global variable
	global labr_class
	global route_class

	# if goroom_class == None:
	# 	goroom_class = GoRoom()

	# if number_of_people == 0:
	# 	number_of_people = goroom_class.main_goroom()

	# change the labdata number of people file with the result of app
	lab_data = pd.read_csv('/home/ec2-user/web/app/labdata.csv')
	lab_data.loc[lab_data["Room"]=="A309","People"] = str(number_of_people)
	lab_data.to_csv('/home/ec2-user/web/app/labdata.csv',index=False)	

	# construct LabRecommend class
	if labr_class == None:
		labr_class = LabRecommend()

	# run the main_lab function from LabRecommend class
	# get all the room_number and lab_name
	room_number, lab_name = labr_class.main_lab()

	# construct RouteRecommend class
	if route_class == None:
		route_class = RouteRecommend()

	# run the main_route function from RouteRecommend class
	# get the route
	route_result = route_class.main_route()

	return render_template('recommendroute.html', room_number = room_number, lab_name = lab_name, route_result = route_result)