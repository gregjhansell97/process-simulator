#outside lib imports
import sys

#inhouse imports
from process import *
from NextFit import *
from FirstFit import *
from BestFit import *

def time_str(time):
	return "time " + str(time) + "ms: "

def sim_started(time, memory):
    print( time_str(time) + "Simulator start (" + str(memory.mem_type) + " -- " + str(memory.algo_type) + ")" )

def proc_arrived(time, letter, size):
	print( time_str(time) + "Process " + str(letter) + " arrived (requires " + str(size) + " frames)" ) 

def proc_added(time, letter):
	print( time_str(time) + "Placed process " + str(letter) + ":" )

def skip_proc(time, letter):
	print( time_str(time) + "Cannot place process " + str(letter) + " -- skipped!" )

def defrag_needed(time, letter):
	print( time_str(time) + "Cannot place process " + str(letter) + " -- starting defragmentation" )

def defrag_complete(time, time_shift, letter, defrag_set):
	print( time_str(time+time_shift) + "Defragmentation complete (moved " + str(time_shift) + " frames: " + str(sorted(defrag_set)) + ")")

def proc_removed(time, letter):
	print( time_str(time) + "Process " + str(letter) + " removed:" )

def sim_ended(time, memory):
    print( time_str(time) + "Simulator ended (" + str(memory.mem_type) + " -- " + str(memory.algo_type) + ")" )

def run_sim(memory, processes):
    time = 0
    sim_started(time, memory)
    while len(processes) > 0:
        i = 0
        #removals first
        while i < len(processes):
            p = processes[i]
            if (p.is_past(time)):
            	del processes[i]
            	continue
            if (p.is_done(time) and p.in_memory):
                memory.remove(p) #remove from memory
                del processes[i]
                proc_removed(time, p.letter)
                print(memory)
                continue
            i += 1
        for p in processes:
            if p.should_start(time):
                proc_arrived(time, p.letter, p.size)
                if p.size > memory.get_total_free_frames(): #skip, there's not enough room
                    skip_proc(time, p.letter)
                    print(memory)
                    continue
                if memory.defrag_needed(p):
                    defrag_needed(time, p.letter)
                    time_shift, defrag_set = memory.defrag()
                    for p_edit in processes:
                        p_edit.shift_time(time, time_shift)
                    defrag_complete(time, time_shift, p.letter, defrag_set) #TODO: need a way to track the frames moved in defragging
                    print(memory)
                    break
                    #needs to handle time shift
                proc_added(time, p.letter)
                memory.add(p)
                time_str(time)
                print(memory)
        time += 1
    sim_ended(time-1, memory)

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
    processes_first = parse_process_file(sys.argv[1])
    processes_next = parse_process_file(sys.argv[1])
    processes_best = parse_process_file(sys.argv[1])

    next_fit_proc = NextFit(256)
    run_sim(next_fit_proc, processes_next)
    first_fit_proc = FirstFit(256)
    run_sim(first_fit_proc, processes_first)
    best_fit_proc = BestFit(256)
    run_sim(best_fit_proc, processes_best)

    #first_fit_test()
    #best_fit_test()
