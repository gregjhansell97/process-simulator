from process import *
import collections

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

		self.mem_list = []
		self.page_table = dict()

		self.mem_type = "Non-contiguous"
		self.algo_type = ""

		for i in range(self.num_frames):
			self.mem_list.append('.')

	def __str__(self):
		returnStr = "="*32
		i = 0
		while (i < self.num_frames):
			if (i%32 == 0):
				returnStr += "\n"
			returnStr += self.mem_list[i]
			i += 1
		returnStr += "\n"
		returnStr += "="*32
		returnStr += "\nPAGE TABLE [page,frame]:"
		for k in sorted(self.page_table.keys()):
			returnStr += "\n" + k + ":"
			for index in range(len(self.page_table[k])):
				l = self.page_table[k][index]
				if index%10 == 0 and index != 0:
					returnStr += "\n"
				else:
					returnStr += " "
				returnStr += "[" + str(l[0]) + "," + str(l[1]) + "]"
		return returnStr

	def defrag_needed(self, p):
		return False

	def defrag(self):
		print("WARNING: SHOULD NEVER BE CALLED")

	#Parameters:
	#process: the process to be removed
	#
	#Return: NA
	def remove(self, p):
		letter = p.letter
		for i in range(len(self.mem_list)):
			if self.mem_list[i] == letter:
				self.mem_list[i] = '.'
		self.page_table.pop(letter, None)
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
		p.in_memory = True
		frame_number = 0
		self.page_table[p.letter] = list()
		for i in range(len(self.mem_list)):
			if frame_number >= p.size:
				break
			if self.mem_list[i] == '.':
				self.mem_list[i] = p.letter
				self.page_table[p.letter].append([frame_number, i])
				frame_number += 1
