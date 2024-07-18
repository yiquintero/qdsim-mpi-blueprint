from mpi4py import MPI
import sys

def print_hello(rank, size, name):
    msg = "Hello World! I am process {0} of {1} on {2}.\n"
    sys.stdout.write(msg.format(rank, size, name))

def print_data(rank, data):
    msg = "Data on process {0} is {1}.\n"
    sys.stdout.write(msg.format(rank, data))

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    comm_size = MPI.COMM_WORLD.Get_size()
    rank = MPI.COMM_WORLD.Get_rank()
    name = MPI.Get_processor_name()
    print_hello(rank, comm_size, name)

    if (rank == 0):
        # Initialize list of dictionaries
        data = [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}]
    else:
        data = None
    
    # Distribute the elements of the list of dictionaries among the ranks
    # This requires: data.size == comm.size
    data = comm.scatter(data, root=0)

    print_data(rank, data)
