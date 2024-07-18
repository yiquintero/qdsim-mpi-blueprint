from mpi4py import MPI
import sys
import qdsimutils
import json

def print_hello(rank, size, name):
    msg = "Hello World! I am process {0} of {1} on {2}.\n"
    sys.stdout.write(msg.format(rank, size, name))

def print_data(rank, data):
    for sim in data:
        msg = "Data on process {0} is {1}.\n"
        sys.stdout.write(msg.format(rank, sim))

def run_parallel_simulation(input_parameters):
    comm = MPI.COMM_WORLD
    comm_size = MPI.COMM_WORLD.Get_size()
    rank = MPI.COMM_WORLD.Get_rank()
    name = MPI.Get_processor_name()
    #print_hello(rank, comm_size, name)
    
    data = qdsimutils.getmysubset(input_parameters, rank, comm_size)
    print_data(rank, data)
