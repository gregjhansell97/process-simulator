#outside lib imports
import sys

#inhouse imports
from process import *

def run_sim(memory, processes):
    pass


if __name__ == "__main__":
    processes = parse_process_file(sys.argv[1])
    for l in processes:
        print(l)
