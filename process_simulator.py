from ghlib import *
from process import *
import sys

def FCFS(process_list):
    clock = 0
    blocked = []
    ready_q = Queue()
    while len(process_list) > 0 or not ready_q.is_empty():
        additions = []












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
