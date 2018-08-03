from threading import Thread
import os

class Th(Thread):
	def __init__(self, num):
		Thread.__init__(self)
		self.num = num
		
	def run(self):
		 os.system("python hack.py")
		 

for x in range(1, 20):
	a = Th(x)
	a.start()
