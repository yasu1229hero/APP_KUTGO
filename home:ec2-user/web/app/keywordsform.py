# This file is not used for the main program. Only sample code
# Code written by Fitra
# Function    : to save the form of keyword
# Output      : reset data of flask form

from flask_wtf import FlaskForm
from wtforms import BooleanField

class KeywordsForm(FlaskForm):
	# initiate the variable of the checklist
	information = BooleanField('Information')
	computer = BooleanField('Computer')
	ai = BooleanField('AI')
	neuralnetwork = BooleanField('Neural Network')
	convolutional = BooleanField('Convolutinal Neural Network')
	braindecoding = BooleanField('Brain Decoding')
	fmri = BooleanField('fMRI')
	wireless = BooleanField('Wireless communication')
	environment = BooleanField('Environment')
	math = BooleanField('Mathematics')
	physics = BooleanField('Physics')
	lifestyle = BooleanField('Lifestyle')
	book = BooleanField('Book')
	office = BooleanField('Office')
	application = BooleanField('Application')
	def reset(self):
		# use the csrf for blankdata
		blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
		self.process(blankData)