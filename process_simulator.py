from ghlib import *
from process import *
import sys

def done(process_list):
    for p in process_list:
        if p.current_num > 0: return False
    return True

def print_simulator_start(clk, algo, q):
    print("time " + str(clk) + "ms: Simulator started for " + algo + " " + str(q))

def print_added_to_ready_queue(clk, p, q):
    print("time " + str(clk) + "ms: Process " + p.id + " arrived and added to ready queue " + str(q))

def print_started_using_cpu(clk, p, q):
    print("time " + str(clk) + "ms: Process " + p.id + " started using the CPU " + str(q))

def print_cpu_burst_completion(clk, p, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " completed a CPU burst; " + str(p.current_num) + " bursts to go " + str(q))

def print_switching_out(clk, p, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " switching out of CPU; will block on I/O until time " + str(clk + p.io_burst + 4) + " " + str(q))

def print_process_terminated(clk, p, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " terminated " + str(q))

def print_completed_io(clk, p, q):
    print("time " + str(clk) + "ms: Process " + str(p.id) + " completed I/O; added to ready queue " + str(q))

def FCFS(process_list):
    pli = 0 #process list index
    clock = 0 #clock
    wait = 0 #used to pause running_process for wait + 1 time
    blocked = [] #list of processes that are blcoking
    ready_q = Queue() #queue of processes in the ready_q
    running_process = None #the current process that is running
    algo = "FCFS" #which algorithm is being used

    print_simulator_start(clock, algo, ready_q)
    #print("time " + str(clock) + "ms: Simulator started for FCFS " + str(ready_q))
    while not done(process_list):
        #process arrive and are added to the queue
        while pli < len(process_list) and process_list[pli].arrival_time == clock:
            ready_q.push(process_list[pli])
            print_added_to_ready_queue(clock, process_list[pli], ready_q)
            #print("time " + str(clock) + "ms: Process " + process_list[pli].id + " arrived and added to ready queue " + str(ready_q))
            pli += 1
        if(wait > 0):
            wait -= 1
        elif running_process is None: #need to set a running process
            if not ready_q.is_empty(): #if there are processes in the ready Q
                wait = 3
                running_process = ready_q.pop()
                print_started_using_cpu(clock + 4, running_process, ready_q)
                #print("time " + str(clock + 4) + "ms: Process " + running_process.id + " started using the CPU " + str(ready_q))
        else: #there is a running_process
            if(running_process.current_burst <= 0): #running process has finished bursts
                if running_process.restart():
                    #print that the process is blocking I/O
                    print_cpu_burst_completion(clock, running_process, ready_q)
                    #print("time " + str(clock) + "ms: Process " + str(running_process.id) + " completed a CPU burst; " + str(running_process.current_num) + " bursts to go " + str(ready_q))
                    print_switching_out(clock, running_process, ready_q)
                    #print("time " + str(clock) + "ms: Process " + str(running_process.id) + " switching out of CPU; will block on I/O until time " + str(clock + running_process.io_burst + 4) + " " + str(ready_q))
                    wait = 3
                    running_process.io_burst += 3 #to add for the wait time
                    blocked.append(running_process)
                else:
                    print_process_terminated(clock, running_process, ready_q)
                    #print("time " + str(clock) + "ms: Process " + str(running_process.id) + " terminated " + str(ready_q))
                    wait = 3
                    #print that the process is terminated
                running_process = None #making sure another process can become running_process
            else: #run process normally by decrementing current_burst
                running_process.current_burst -= 1

        #handle blocked list
        i = 0
        while i < len(blocked): #looping through blocks
            if blocked[i].io_burst <= 0: #if I/O is done
                change_process = blocked.pop(i)
                ready_q.push(change_process)
                print_completed_io(clock + 1, change_process, ready_q)
                #print("time " + str(clock + 1) + "ms: Process " + str(change_process.id) + " completed I/O; added to ready queue " + str(ready_q))
                continue
            else: #if I/O burst needs more time
                blocked[i].io_burst -= 1
            i += 1
        clock += 1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        #definetly not the best way to error handle
        print("ERROR takes in only two arguments")
        sys.exit(1)

    f = open(sys.argv[1])
    process_list = []
    for line in f:
        if len(line) == 0 or line[0] == "#": continue
        process_list.append(Process(line))
    FCFS(process_list)
