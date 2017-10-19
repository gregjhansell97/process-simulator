'''
Shane O'Brien && Greg Hansell
Operating Systems - CSCI 4210
Project One
'''

from ghlib import *
from process import *
from info import *
import sys
import copy

t_slice = 70

def done(process_list):
    for p in process_list:
        if p.current_num > 0: return False
    return True

def getTotalNum(process_list):
    totalNum = 0
    for p in process_list:
        totalNum += p.num_bursts
    return totalNum

def print_simulator_start(clk, algo, q):
    print("time " + str(clk) + "ms: Simulator started for " + algo + " " + str(q))

def print_added_to_ready_queue(clk, p, q):
    print("time " + str(clk) + "ms: Process " + p.id + " arrived and added to ready queue " + str(q))

def print_started_using_cpu(clk, p, q):
    if (p.current_burst == p.burst_time):
        print("time " + str(clk) + "ms: Process " + p.id + " started using the CPU " + str(q))
    else:
        print("time " + str(clk) + "ms: Process " + p.id + " started using the CPU with " + str(p.current_burst) + "ms remaining " + str(q))

def print_cpu_burst_completion(clk, p, q):
    if (p.current_num == 1):
        print("time " + str(clk) + "ms: Process " + str(p.id) + " completed a CPU burst; " + str(p.current_num) + " burst to go " + str(q))
    else:
        print("time " + str(clk) + "ms: Process " + str(p.id) + " completed a CPU burst; " + str(p.current_num) + " bursts to go " + str(q))

def print_switching_out(clk, p, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " switching out of CPU; will block on I/O until time " + str(clk + p.io_burst + 4) + "ms " + str(q))

def print_process_terminated(clk, p, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " terminated " + str(q))

def print_completed_io(clk, p, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " completed I/O; added to ready queue " + str(q))

def print_simulator_finish(clk, algo, q):
    print("time " + str(clk) + "ms: Simulator ended for " + algo)

def print_preemption(clk, p, rp, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " arrived and will preempt " +str(rp.id) + " " + str(q))

def print_preempt_io(clk, p, rp, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " completed I/O and will preempt " +str(rp.id) + " " + str(q))

def print_started_using_cpu_preempt(clk, p, q):
    print("time " + str(clk) + "ms: Process " + p.id + " started using the CPU with " + str(p.current_burst) + "ms remaining " + str(q))

def print_tslice_expire_add(clk, p, q):
    print("time " + str(clk) + "ms: Time slice expired; process " + str(p.id) + " preempted with " + str(p.current_burst) + "ms to go " + str(q))

def print_tslice_expire_noadd(clk, p, q):
    print("time " + str(clk) + "ms: Time slice expired; no preemption because ready queue is empty " + str(q))

def FCFS(process_list):
    pli = 0 #process list index
    clock = 0 #clock
    wait = 0 #used to pause running_process for wait + 1 time
    blocked = [] #list of processes that are blcoking
    ready_q = Queue() #queue of processes in the ready_q
    running_process = None #the current process that is running
    algo = "FCFS" #which algorithm is being used

    print_simulator_start(clock, algo, ready_q)
    while not done(process_list):

        #process arrive and are added to the queue
        while pli < len(process_list) and process_list[pli].arrival_time == clock:
            ready_q.push(process_list[pli])
            print_added_to_ready_queue(clock, process_list[pli], ready_q)
            pli += 1

        if(wait > 0):
            wait -= 1
        elif running_process is None: #need to set a running process
            if not ready_q.is_empty(): #if there are processes in the ready Q
                wait = 3
                FCFSinfo.turnaround_time += 4
                running_process = ready_q.pop()
                print_started_using_cpu(clock + 4, running_process, ready_q)
        else: #there is a running_process
            if(running_process.current_burst <= 0): #running process has finished bursts
                if running_process.restart():
                    #print that the process is blocking I/O
                    print_cpu_burst_completion(clock, running_process, ready_q)
                    print_switching_out(clock, running_process, ready_q)
                    wait = 3
                    FCFSinfo.turnaround_time += 4
                    running_process.io_burst += 3 #to add for the wait time
                    blocked.append(running_process)
                else:
                    print_process_terminated(clock, running_process, ready_q)
                    wait = 3
                    FCFSinfo.turnaround_time += 4
                    #print that the process is terminated
                FCFSinfo.num_contextswitches += 1
                running_process = None #making sure another process can become running_process
            else: #run process normally by decrementing current_burst
                FCFSinfo.burst_time += 1 #count the running_process
                FCFSinfo.turnaround_time += 1 #count for running process
                running_process.current_burst -= 1

        FCFSinfo.wait_time += int(ready_q.length()) #count for all processes in queue
        FCFSinfo.turnaround_time += int(ready_q.length()) #count for all processes in queue
        
        ##CYCLE CONSIDERED DONE HERE##
        #handle blocked list
        i = 0
        while i < len(blocked): #looping through blocks
            if blocked[i].io_burst <= 0: #if I/O is done
                change_process = blocked.pop(i)
                ready_q.push(change_process)
                print_completed_io(clock + 1, change_process, ready_q)
                continue
            else: #if I/O burst needs more time
                blocked[i].io_burst -= 1
            i += 1
        clock += 1

    clock += wait
    print_simulator_finish(clock, algo, ready_q)    

def SRT(process_list):
    pli = 0 #process list index
    clock = 0 #clock
    wait = 0 #used to pause running_process for wait + 1 time
    blocked = [] #list of processes that are blcoking
    pq = Priority_Queue()
    running_process = None #the current process that is running
    algo = "SRT" #which algorithm is being used

    print_simulator_start(clock, algo, pq)
    while not done(process_list):
        #process arrive and are added to the queue
        while pli < len(process_list) and process_list[pli].arrival_time == clock:
            pq.push(process_list[pli])
            #if there is a running process, and the newly added process needs to preempt it
            if (running_process is not None):
                if (process_list[pli].current_burst < running_process.current_burst):
                    print_preemption(clock, process_list[pli], running_process, pq)
                    pq.push(running_process)
                    SRTinfo.num_preemptions += 1
                    SRTinfo.num_contextswitches += 1
                    SRTinfo.wait_time -= 8 #because you are putting two on pq and making it wait for 4 ms
                    wait = 4
                    running_process = None
                else:
                    print_added_to_ready_queue(clock, process_list[pli], pq)
            else:
                print_added_to_ready_queue(clock, process_list[pli], pq)
            pli += 1

        if(wait > 0):
            wait -= 1
        elif running_process is None: #need to set a running process
            if not pq.is_empty(): #if there are processes in the ready Q
                wait = 3
                SRTinfo.turnaround_time += 4
                running_process = pq.pop()
                if (running_process.current_burst < running_process.burst_time):
                    print_started_using_cpu_preempt(clock + 4, running_process, pq)
                else:
                    print_started_using_cpu(clock + 4, running_process, pq)
        else: #there is a running_process
            if(running_process.current_burst <= 0): #running process has finished bursts
                if running_process.restart():
                    print_cpu_burst_completion(clock, running_process, pq)
                    print_switching_out(clock, running_process, pq)
                    SRTinfo.turnaround_time += 4
                    wait = 3
                    running_process.io_burst += 3 #to add for the wait time
                    blocked.append(running_process)
                else:
                    print_process_terminated(clock, running_process, pq)
                    SRTinfo.turnaround_time += 4
                    wait = 3
                    #print that the process is terminated
                SRTinfo.num_contextswitches += 1
                running_process = None #making sure another process can become running_process
            else: #run process normally by decrementing current_burst
                SRTinfo.burst_time += 1 #count the running_process
                SRTinfo.turnaround_time += 1 #count for running process
                running_process.current_burst -= 1

        #CYCLE CONSIDERED DONE HERE#

        SRTinfo.wait_time += int(pq.length())
        SRTinfo.turnaround_time += int(pq.length()) #count for all processes in queue
        
        #COUNT DONE HERE#

        #handle blocked list
        i = 0
        while i < len(blocked): #looping through blocks
            if blocked[i].io_burst <= 0: #if I/O is done
                change_process = blocked.pop(i)
                if (running_process is not None):
                    if (change_process.current_burst < running_process.current_burst):
                        print_preempt_io(clock + 1, change_process, running_process, pq)
                        pq.push(running_process)
                        SRTinfo.wait_time -= 8 #because you are putting two on pq and making it wait for 4 ms
                        SRTinfo.num_preemptions += 1
                        SRTinfo.num_contextswitches += 1
                        wait = 4
                        running_process = None
                    else:
                        print_completed_io(clock + 1, change_process, pq)
                else:
                    print_completed_io(clock + 1, change_process, pq)
                pq.push(change_process)
                continue
            else: #if I/O burst needs more time
                blocked[i].io_burst -= 1
            i += 1
        clock += 1

    clock += wait
    print_simulator_finish(clock, algo, pq)

def RR(process_list):
    pli = 0 #process list index
    clock = 0 #clock
    wait = 0 #used to pause running_process for wait + 1 time
    blocked = [] #list of processes that are blcoking
    ready_q = Queue() #queue of processes in the ready_q
    running_process = None #the current process that is running
    timeslice_counter = 0 #keeps track of current CPU time
    algo = "RR" #which algorithm is being used

    print_simulator_start(clock, algo, ready_q)
    while not done(process_list):
        #process arrive and are added to the queue
        while pli < len(process_list) and process_list[pli].arrival_time == clock:
            ready_q.push(process_list[pli])
            print_added_to_ready_queue(clock, process_list[pli], ready_q)
            pli += 1

        if(wait > 0):
            wait -= 1
        elif running_process is None: #need to set a running process
            if not ready_q.is_empty(): #if there are processes in the ready Q
                wait = 3
                RRinfo.turnaround_time += 4
                running_process = ready_q.pop()
                print_started_using_cpu(clock + 4, running_process, ready_q)
                timeslice_counter = 0
        else: #there is a running_process
            if(running_process.current_burst <= 0): #running process has finished bursts
                if running_process.restart():
                    #print that the process is blocking I/O
                    print_cpu_burst_completion(clock, running_process, ready_q)
                    print_switching_out(clock, running_process, ready_q)
                    wait = 3
                    RRinfo.turnaround_time += 4
                    running_process.io_burst += 3 #to add for the wait time
                    blocked.append(running_process)
                    timeslice_counter = 0
                else:
                    print_process_terminated(clock, running_process, ready_q)
                    wait = 3
                    RRinfo.turnaround_time += 4
                    #print that the process is terminated
                RRinfo.num_contextswitches += 1
                running_process = None #making sure another process can become running_process
            elif(timeslice_counter >= t_slice):
                if (ready_q.is_empty()): #if the queue is empty, just keep running the process
                    print_tslice_expire_noadd(clock, running_process, ready_q)
                    RRinfo.burst_time += 1
                    RRinfo.turnaround_time += 1
                    running_process.current_burst -= 1
                    timeslice_counter = 1
                else:
                    print_tslice_expire_add(clock, running_process, ready_q)
                    RRinfo.num_preemptions += 1
                    RRinfo.num_contextswitches += 1
                    RRinfo.wait_time -= 4
                    ready_q.push(running_process)
                    wait = 3
                    running_process = None
                    timeslice_counter = 0
            else: #run process normally by decrementing current_burst
                RRinfo.burst_time += 1 #count the running_process
                RRinfo.turnaround_time += 1 #count for running process
                timeslice_counter += 1
                running_process.current_burst -= 1

        RRinfo.wait_time += int(ready_q.length())
        RRinfo.turnaround_time += int(ready_q.length()) #count for all processes in queue

        #handle blocked list
        i = 0
        while i < len(blocked): #looping through blocks
            if blocked[i].io_burst <= 0: #if I/O is done
                change_process = blocked.pop(i)
                print_completed_io(clock + 1, change_process, ready_q)
                ready_q.push(change_process)
                continue
            else: #if I/O burst needs more time
                blocked[i].io_burst -= 1
            i += 1
        clock += 1

    clock += wait
    print_simulator_finish(clock, algo, ready_q)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        #definetly not the best way to error handle
        print("ERROR: Invalid arguments")
        print("USAGE: ./a.out <input-file> <stats-output-file>")
        sys.exit(1)
    if (sys.argv[1][-4:] != ".txt"):
        print("ERROR: Invalid input file format")
        sys.exit(1)

    f = open(sys.argv[1])
    process_listFCFS = []
    process_listSRT = []
    process_listRR = []
    for line in f:
        if len(line) == 0 or line[0] == "#" or line[0] == '\n': continue
        process_listFCFS.append(Process(line))
        process_listSRT.append(Process(line))
        process_listRR.append(Process(line))

    #making the info objects
    numProcesses = getTotalNum(process_listRR)
    FCFSinfo = Info("FCFS", numProcesses)
    SRTinfo = Info("SRT", numProcesses)
    RRinfo = Info("RR", numProcesses)

    #running the process simulations
    FCFS(process_listFCFS)
    print()
    SRT(process_listSRT)
    print()
    RR(process_listRR)
    
    # #adding the info to the output text file
    # print(str(FCFSinfo))
    # print(str(SRTinfo))
    # print(str(RRinfo))
    f2 = open(sys.argv[2], 'w')
    f2.write(str(FCFSinfo))
    f2.write(str(SRTinfo))
    f2.write(str(RRinfo))
    f2.close()