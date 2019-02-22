#coding:utf8

class NkLibrary(Qwidget):
	def __init__(self):
		super(NkLibrary, self).__init__()
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")


		# 이벤트 설정
		self.ok.clicked.connect(self.pushOK)
		self.cancel.clicked.connect(self.close)
		# layout 설정
		layout = QGridLayout()
		layout.addWidget(self.cancel, 1, 0)
		layout.addWidget(self.ok, 1, 1)

	def pushOK(self):
	"""
	OK 버튼을 누르면, 파일을 불러온다.
	"""

	self.close()


def main():
	NKLibrary()








