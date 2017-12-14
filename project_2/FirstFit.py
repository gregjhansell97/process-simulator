from ContMem import *
from process import *

#FirstFit:
#builds on the ContMem class
class FirstFit(ContMem):
	def __init__(self, num_framesI):
		ContMem.__init__(self, num_framesI)


	def defragNeeded(self, p):
		free_frame_count = 0 #counts the number of free frames in a row
		for frame in self.mem_list:#iterates throught he frames of memory
			if frame == '.': #'.' signifies and empty frame
				free_frame_count += 1
			else:
				free_frame_count = 0
			if free_frame_count >= p.size:
				return False
		return True


	#Parameters:
	#process: the process to be added
	#
	#Return: NA
	def add(self, Process):
		length = Process.size
		letter = str(Process)
		i = 0
		while(i < self.num_frames):
			i = self.find_process('.', i)

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
