#!/bin/bash
#SBATCH -J singularity                 # Job name
#SBATCH -o singularity.txt             # Output file name
#SBATCH -p container                   # Partition (queue)
#SBATCH -c 1                           # Cores requested
#SBATCH --mem=6G                       # Total memory required per node

module purge                           # Unload all modules
module load singularity/3.5.3          # Load Singularity

./anaconda.sif matrix_multiplication.py # Run container

