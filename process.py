class Process(object):
    '''
    parameters: string s, that's a file string
    purpose:
    state variables:
        id: process's id like A, B, C ...
        arrival_time: when the process gets added to the queue
        burst_time: how much time it needs with the cpu
        num_bursts: how many bursts are needed
        io_time: After finish each burst, how much of a wait till added back
            into the queue
    '''
    def __init__(self, s):
        l = s.split("|")

        #don't modify
        self.id = l[0]
        self.arrival_time = int(l[1])
        self.burst_time = int(l[2])
        self.num_bursts = int(l[3])
        self.io_time = int(l[4])

        #modify
        self.io_burst = self.io_time
        self.current_burst = self.burst_time
        self.current_num = self.num_bursts
    '''
    parameters: <none>
    purpose: converts a Process object into a string value
    returns: string representation of the Process
    '''
    def __str__(self):
        return self.id + "|" + str(self.arrival_time) + "|" + str(self.burst_time) + "|" + str(self.current_num) + "|" + str(self.io_time)

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __eq__(self, other):
        return False

    '''
    parameters: <none>
    purpose: called after it finishes current bursts
    returns: boolean (whether or not the process is completely finished)
    '''
    def restart(self):
        self.current_num -= 1
        if self.current_num == 0:
            return False
        self.current_burst = self.burst_time
        self.io_burst = self.io_time
        return True
