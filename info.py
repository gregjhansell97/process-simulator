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
    	toprint += "-- average CPU burst time: " + str(self.avg_burst_time/self.num_processes) + "ms\n"
    	toprint += "-- average wait time: " + str(self.avg_wait_time/self.num_processes) + "ms\n"
    	toprint += "-- average turnaround time: " + str(self.avg_turnaround_time/self.num_processes) + "ms\n"
    	toprint += "-- total number of context switches: " + str(self.num_contextswitches) + "ms\n"
    	toprint += "-- total number of preemptions: " + str(self.num_preemptions) + "ms\n"
    	return toprint