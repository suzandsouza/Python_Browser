#https://www.youtube.com/watch?v=z-5bZ8EoKu4&t=1278s
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('https://google.com'))
		self.setCentralWidget(self.browser)
		self.showMaximized()
		#to have a desktop size window

		#navbar
		navbar = QToolBar()
		self.addToolBar(navbar)

		back_btn = QAction('Back', self)
		back_btn.triggered.connect(self.browser.back)
		navbar.addAction(back_btn)

		forward_btn = QAction('Forward', self)
		forward_btn.triggered.connect(self.browser.forward)
		navbar.addAction(forward_btn)

		reload_btn = QAction('Reload', self)
		reload_btn.triggered.connect(self.browser.reload)
		navbar.addAction(reload_btn)

		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.navigate_to_url)
		navbar.addWidget(self.url_bar)

		self.browser.urlChanged.connect(self.update_url)


	def navigate_to_url(self):
		url = self.url_bar.text()
		self.browser.setUrl(QUrl(url))

	def update_url(self, q):
		self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
window = MainWindow()
app.exec()
