#coding:utf8
import os
from PySide2.QtWidgets import *

class CheckEnv(QWidget):
	def __init__(self):
		super(CheckEnv, self).__init__()
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.setSen()

	def setSen(self):
		sentence = "hello world"
		self.layout.addWidget(QLabel("%s" % sentence))

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = CheckEnv()
	try:
		customApp.show()
	except:
		pass
