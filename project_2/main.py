#outside lib imports
import sys

#inhouse imports
from process import *
from NextFit import *

def run_sim(memory, processes):
    pass


if __name__ == "__main__":
	processes = parse_process_file(sys.argv[1])
	for l in processes:
		print(l)

	testProc = NextFit(256)
	print(testProc)

	testProc.add(processes[0])
	print(testProc)
	testProc.add(processes[1])
	print(testProc)
	testProc.remove('A')
	print(testProc)
	testProc.add(processes[3])
	print(testProc)

