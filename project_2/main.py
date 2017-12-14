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
    print(time_str(time) + "Simulator started ")# we need some way to get simulator started
    while len(processes) > 0:
        i = 0
        #removals first
        while i < len(processes):
            p = processes[i];
            if p.isDone(time):
                memory.remove(p) #remove from memory
                del processes[i]
                print(time_str(time))
                print(memory)
                continue
            i += 1
        for p in processes:
            if p.shouldStart(time):
                if p.size > memory.get_total_free_frames(): #skip, there's not enough room
                    print(time_str(time))
                    print(memory)
                    continue
                if memory.defragNeeded(p):
                    time_shift = memory.defrag()
                    for p_edit in processes:
                        p_edit.shiftTime(time, time_shift)
                    print(time_str(time))
                    print(memory)
                    break
                    #needs to handle time shift
                memory.add(p)
                print(time_str(time))
                print(memory)
        time += 1

def first_fit_test():
    testProc = FirstFit(256)
    print(testProc)

    testProc.add(processes[0])
    print(testProc)

    testProc.add(processes[1])
    print(testProc)

    testProc.remove(processes[0])
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

    testProc = FirstFit(256)
    #print(testProc)
    run_sim(testProc, processes)
    #first_fit_test()
    #best_fit_test()
