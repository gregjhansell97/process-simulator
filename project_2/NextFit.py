from ContMem import *
from process import *

#NextFit:
#builds on the ContMem class
#Variables:
#algo-type: for printing in main
class NextFit(ContMem):
	def __init__(self, num_framesI):
		ContMem.__init__(self, num_framesI)
		self.algo_type = " -- Next-Fit"
		self.last_point = 0

	def enough_room(self, index, size):
		if index + size > len(self.mem_list):
			return False
		for i in range(index, index + size):
			if self.mem_list[i] != '.':
				return False
		return True

	def add(self, p):
		while True:
			if self.enough_room(self.last_point, p.size):
				for i in range(self.last_point, self.last_point + p.size):
					self.mem_list[i] = p.letter
					self.last_point += 1
				p.in_memory = True
				return
			self.last_point = (self.last_point + 1)*(self.last_point < (len(self.mem_list) - 1))

	def defrag(self):
		defrag_set = set()
		total_count = 0
		while (1):
			count = self.move(defrag_set)
			if (count > 0):
				total_count += count
			else:
				break

		#reset the current frame
		self.current_frame = self.find_process('.', 0)
		self.last_point = 0
		return (total_count, defrag_set)

	#Parameters:
	#process: the process to be added
	#
	#Return: NA
	'''
	def add(self, p):
		length = p.size
		letter = str(p)
		i = self.current_frame
		#print("self.current_frame1: ", self.current_frame)
		while(i < self.num_frames):
			i = self.find_process('.', i)

			#print("i: ", i)

			#if nextfit gets to end, goes back to beginning and looks again
			if (i == (self.num_frames)-1 or i == (self.num_frames)):
				i = 0
				#print("ay")
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

		#setting the starting location for the next add. accounts for if add goes to end of memory
		if (i == 256):
			self.current_frame = 0
		else:
			self.current_frame = i

		p.in_memory = True
		#print("self.current_frame2: ", self.current_frame)
		'''
