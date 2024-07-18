#!/bin/bash
#SBATCH --job-name="qdsim-mpi"
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4     # 4 mpi processes
#SBATCH --cpus-per-task=1       # because no threading
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=compute

# Load modules:
module load miniconda3

# Set conda env:
# see https://doc.dhpc.tudelft.nl/delftblue/howtos/conda/
unset CONDA_SHLVL
source "$(conda info --base)/etc/profile.d/conda.sh"

# Activate conda, run job, deactivate conda
conda activate qdsim-mpi
mpirun -np 4 python helloworld.py
conda deactivate

seff $SLURM_JOB_ID