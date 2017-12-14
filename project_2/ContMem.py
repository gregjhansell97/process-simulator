from process import *

#This class describes the attributes of a general Memory Class and its children
#Variables:
#num_frames: number of frames in memory
#max_num_processes: number of different processes we allow in the memory
#t_memmove: for defragging. the time it takes to move one frame
#mem_list: the actual memory as a list
#current_frame: important for algorithms that keep track of order when adding processes
class ContMem(object):
	#Parameters
	#num_framesI: the number of frames to be allocated for memory
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

	#Parameters:
	#process: the process to be removed
	#
	#Return: NA
	def remove(self, p):
		letter = p.letter
		for i in range(len(self.mem_list)):
			if self.mem_list[i] == letter:
				self.mem_list[i] = '.'
		'''start_point = self.find_process(Process, 0)

		i = start_point
		while (i < self.num_frames):
			if (self.mem_list[i] != str(Process) or self.mem_list[i] == '.'):
				break
			self.mem_list[i] = '.'
			i += 1'''

	#Parameters:
	#
	#Return: the number of total frames that are free. helpful to know before defragging
	def get_total_free_frames(self):
		total_free = 0
		for frame in self.mem_list:
			if frame == '.':
				total_free += 1
		return total_free

	#Parameters:
	#
	#Return: total number of frames moved. returns 0 if no moving needed
	def move(self):
		#seeing if a move needs to happen
		i = 0
		first_dot = 0
		while (i < self.num_frames):
			if (self.mem_list[i] == '.'):
				first_dot = i
				break
			i += 1

		first_letter = 0
		while (i < self.num_frames):
			if (self.mem_list[i] != '.'):
				first_letter = i
				break
			i += 1

		if (first_letter == 0):
			return 0

		#move first_letter into first_dot
		letter = self.mem_list[first_letter]
		count = 0
		while (1):
			if (self.mem_list[first_letter] == letter):
				self.mem_list[first_dot] = letter
				self.mem_list[first_letter] = '.'
				first_dot += 1
				first_letter += 1
				count += 1
			else:
				break
		return count

	#Parameters:
	#
	#Return: handles the defragging and returns the total number of moves occured.
	#		if no moves occurred, 0 is returned
	def defrag(self):
		total_count = 0
		while (1):
			count = self.move()
			if (count > 0):
				total_count += count
			else:
				break

		#reset the current frame
		self.current_frame = self.find_process('.', 0)

		return total_count
