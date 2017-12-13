from ContMem import *
from process import *

class NextFit(ContMem):
	def __init__(self, num_framesI):
		ContMem.__init__(self, num_framesI)

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


