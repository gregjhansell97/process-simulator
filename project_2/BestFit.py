from ContMem import *
from process import *

#BestFit:
#builds on the ContMem class
class BestFit(ContMem):
	def __init__(self, num_framesI):
		ContMem.__init__(self, num_framesI)
		self.algo_type = "Best-Fit"

	#Parameters:
	#pointer: the beginning of a chunk of free memory
	#length: the length needed for the process to be added
	#
	#Return: checks how long until a letter occurs in memory1
	def check_for_letter(self, pointer, length):
		i = pointer
		count = 0
		while (i < self.num_frames):
			if (self.mem_list[i] != '.'):
				break
			count += 1
			i += 1

		return count

	#Parameters:
	#process: the process to be added
	#
	#Return: NA
	def add(self, p):
		#find list of all potential landing spots bigger than the lenght of the p
		i = 0
		list_of_potentials = []
		while (i < self.num_frames):
			i = self.find_p('.', i)
			count = self.check_for_letter(i, p.size)
			if (count >= p.size):
				list_of_potentials.append([i, count])
			i += count
			i += 1

		#print("list_of_potentials: ", list_of_potentials)

		#get the spot where the p will be added
		i = 0
		min_num = 65536
		min_spot = 0
		while (i < len(list_of_potentials)):
			if (list_of_potentials[i][1] < min_num):
				min_num = list_of_potentials[i][1]
				min_spot = i
			i += 1
		spot_to_add = list_of_potentials[min_spot][0]

		#add p to memory
		i = spot_to_add
		while (i < spot_to_add+p.size):
			self.mem_list[i] = str(p)
			i += 1

		p.in_memory = True