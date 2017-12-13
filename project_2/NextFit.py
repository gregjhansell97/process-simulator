from ContMem import *
from process import *

#NextFit:
#builds on the ContMem class
class NextFit(ContMem):
	def __init__(self, num_framesI):
		ContMem.__init__(self, num_framesI)

	#Parameters:
	#process: the process to be added
	#
	#Return: NA
	def add(self, Process):
		length = Process.size
		letter = str(Process)
		i = self.current_frame	
		while(i < self.num_frames):
			i = self.find_process('.', i)

			#if nextfit gets to end, goes back to beginning and looks again
			if (i == self.num_frames-1):
				i = 0
				continue

			j = 0
			intheclear = False
			while(j != self.num_frames-i):
				if (self.mem_list[i+j] == '.'):
					j += 1
					if (j == length):
						intheclear = True
						break
				if (self.mem_list[i+j] != '.'):
					i += j
					break
	
			if (intheclear):
				#print("locationtoadd: ", i)
				break

		start = i
		while (i < start+length):
			#print("i: ", i)
			self.mem_list[i] = str(letter)
			i += 1

		#setting the starting location for the next add
		self.current_frame = i
