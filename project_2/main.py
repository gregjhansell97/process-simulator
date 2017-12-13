#outside lib imports
import sys

#inhouse imports
from process import *
from NextFit import *
from FirstFit import *
from BestFit import *

def run_sim(memory, processes):
    pass

def first_fit_test():
	testProc = FirstFit(256)
	print(testProc)

	testProc.add(processes[0])
	print(testProc)

	testProc.add(processes[1])
	print(testProc)

	testProc.remove('A')
	print(testProc)

	testProc.add(processes[3])
	print(testProc)

	num_delay = testProc.defrag()
	print(testProc)
	print("num_delay: ", num_delay)

	testProc.add(processes[1])
	print(testProc)

	testProc.remove('D')
	print(testProc)

	num_delay = testProc.defrag()
	print(testProc)
	print("num_delay: ", num_delay)

def best_fit_test():
	testProc = BestFit(256)

	testProc.add(processes[0])
	print(testProc)

	testProc.add(processes[1])
	print(testProc)

	testProc.add(processes[3])
	print(testProc)

	testProc.add(processes[0])
	print(testProc)

	testProc.add(processes[1])
	print(testProc)

	testProc.remove('A')
	print(testProc)

	testProc.add(processes[7])
	print(testProc)

if __name__ == "__main__":
	processes = parse_process_file(sys.argv[1])
	for l in processes:
		print(l)

	#first_fit_test()
	best_fit_test()

