from ContMem import *
from process import *

#NextFit:
#builds on the ContMem class
class NextFit(ContMem):
	def __init__(self, num_framesI):
		ContMem.__init__(self, num_framesI)
		self.algo_type = "Next-Fit"

	#Parameters:
	#process: the process to be added
	#
	#Return: NA
	def add(self, p):
		length = p.size
		letter = str(p)
		i = self.current_frame
		print("self.current_frame1: ", self.current_frame)	
		while(i < self.num_frames):
			i = self.find_process('.', i)

			print("i: ", i)

			#if nextfit gets to end, goes back to beginning and looks again
			if (i == (self.num_frames)-1 or i == (self.num_frames)):
				i = 0
				print("ay")
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
		if (i == 256):
			self.current_frame = 0
		else:
			self.current_frame = i

		p.in_memory = True
		print("self.current_frame2: ", self.current_frame)	
