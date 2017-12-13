#outside lib imports
import sys

#inhouse imports
from process import *
from NextFit import *
from FirstFit import *
from BestFit import *
def time_str(time):
    return "time " + str(time) + "ms: "

def run_sim(memory, processes):
    time = 0
    print(time_str(time) + "Simulator started " + str(memory))
    while len(processes) > 0:
        i = 0
        #endles removals first
        while i < len(processes):
            p = processes[i];
            if p.isDone(time):
                memory.remove(p) #remove from memory
                del processes[i]
                continue
        for p in processes:
            if p.shouldStart(time):
                #needs to deal with memory defragmentaiton
                memory.add(p)


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
