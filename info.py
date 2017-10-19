class Info(object):
    '''
    parameters: <none>
    purpose: default constructor that creates all the info we want to hold to print out
    '''
    def __init__(self, algo, num):
    	self.type = algo
    	self.avg_burst_time = 0
    	self.avg_wait_time = 0
    	self.avg_turnaround_time = 0
    	self.num_contextswitches = 0
    	self.num_preemptions = 0

    	#print("num: ", num)
    	self.num_processes = num
    	#print("self.num_processes: ", self.num_processes)

    '''
    parameters: <none>
    purpose: print statement
    '''
    def __str__(self):
    	toprint = "Algorithm " + str(self.type) + "\n"
    	toprint += "-- average CPU burst time: " + str(round(self.avg_burst_time/self.num_processes, 2)) + "ms\n"
    	toprint += "-- average wait time: " + str(round(self.avg_wait_time/self.num_processes, 2)) + "ms\n"
    	toprint += "-- average turnaround time: " + str(round(self.avg_turnaround_time/self.num_processes, 2)) + "ms\n"
    	toprint += "-- total number of context switches: " + str(self.num_contextswitches) + "\n"
    	toprint += "-- total number of preemptions: " + str(self.num_preemptions) + "\n"
    	return toprint