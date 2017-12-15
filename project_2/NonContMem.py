from process import *

#This class describes the attributes of a non-contiguous memory class
#Variables:
#num_frames: number of frames in memory
#max_num_processes: number of different processes we allow in the memory
#t_memmove: for defragging. the time it takes to move one frame
#mem_list: the actual memory as a list
#current_frame: important for algorithms that keep track of order when adding processes
#mem-type: for printing in main
#algo-type: for printint in main
class NonContMem(object):
	#Parameters
	#num_framesI: the number of frames to be allocated for memory
	def __init__(self, num_framesI):
		self.num_frames = num_framesI
		self.max_num_processes = 26
		self.t_memmove = 1

		self.mem_list = []
		self.current_frame = 0

		self.mem_type = "Non-contiguous"
		self.algo_type = ""

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

		#also add onto return string page count

		return returnStr

	#Parameters:
	#letter: the letter of the process
	#
	#Return: returns the location in memory after start that has letter
	def find_process(self, p, start):
		i = start
		while (i < self.num_frames):
			if (self.mem_list[i] == str(p)):
				break
			i += 1
		return i

	#Parameters:
	#process: the process to be removed
	#
	#Return: NA
	def remove(self, p):
		letter = p.letter
		for i in range(len(self.mem_list)):
			if self.mem_list[i] == letter:
				self.mem_list[i] = '.'

		p.in_memory = False

	#Parameters:
	#
	#Return: the number of total frames that are free.
	def get_total_free_frames(self):
		total_free = 0
		for frame in self.mem_list:
			if frame == '.':
				total_free += 1
		return total_free

	def add(self, p):
		pass
		#make add here. biggest part of noncontig