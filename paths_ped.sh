#! /bin/bash
#SBATCH -A spnmmd


# This makes a text file called Paths_to_peds.txt

Out=$1


python3.6 Py_scripts/path_to_sim.py -o ${Out} 