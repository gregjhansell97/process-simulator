#This class describes the attributes of a general Memory Class and its children
#Variables:
#num_frames: number of frames in memory

from process import *

class ContMem(object):
	#Parameters
	#num_framesI: 
	def __init__(self, num_framesI):
		self.num_frames = num_framesI
		self.max_num_processes = 26
		self.t_memmove = 1

		self.mem_list = []
		self.current_frame = 0

		i = 0
		while (i < self.num_frames):
			self.mem_list.append('.')
			i += 1

	def __str__(self):
		returnStr = "================"
		i = 0
		while (i < self.num_frames):
			if (i%16 == 0):
				returnStr += "\n"
			returnStr += self.mem_list[i]
			i += 1
		returnStr += "\n================"
		return returnStr

	#Parameters:
	#letter: the letter of the process
	#
	#Return: returns the location in memory after start that has letter
	def find_process(self, Process, start):
		i = start
		while (i < self.num_frames):
			if (self.mem_list[i] == str(Process)):
				break
			i += 1
		return i

	def remove(self, Process):
		start_point = self.find_process(Process, 0)

		i = start_point
		while (i < self.num_frames):
			if (self.mem_list[i] != str(Process) or self.mem_list[i] == '.'):
				break
			self.mem_list[i] = '.'
			i += 1

	def defrag_check(self):
		pass
		#run through and see if defragging is done

	def defrag(self):
		time = 0

		dot_pointer = 0
		letter_pointer = 0

		#have completed check
		i = 0
		while (i < self.num_frames):
			
			i += 1

		i = 0
		#move processes up one at a time
		#reset pointer
		#return time it took

