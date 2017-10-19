class Info(object):
    '''
    parameters: algo-name of algorithm used, num-total number of processes A+B+C,etc...
    purpose: default constructor that creates all the info we want to hold to print out
    '''
    def __init__(self, algo, num):
    	self.type = algo
    	self.burst_time = 0
    	self.wait_time = 0
    	self.turnaround_time = 0
    	self.num_contextswitches = 0
    	self.num_preemptions = 0

    	#total number of processes
    	self.num_processes = num

    '''
    parameters: <none>
    purpose: print statement.
    explanation: i am dividing by self.num_processes because the burst time and such were just totals. we
    need the averages per process
    '''
    def __str__(self):
    	toprint = "Algorithm " + str(self.type) + "\n"
    	toprint += "-- average CPU burst time: " + str(round(self.burst_time/self.num_processes, 2)) + "ms\n"
    	toprint += "-- average wait time: " + str(round(self.wait_time/self.num_processes, 2)) + "ms\n"
    	toprint += "-- average turnaround time: " + str(round(self.turnaround_time/self.num_processes, 2)) + "ms\n"
    	toprint += "-- total number of context switches: " + str(self.num_contextswitches) + "\n"
    	toprint += "-- total number of preemptions: " + str(self.num_preemptions) + "\n"
    	return toprint