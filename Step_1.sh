#! /bin/bash
#SBATCH -A spnmmd


# This runs the simulation for the number passed by array ID

module load merlin

Out=$1

echo ${SLURM_ARRAY_TASK_ID}

N=${SLURM_ARRAY_TASK_ID}

python3.6 /Py_scrpts/step_1.py -o ${Out} -n ${N}

wait

echo "Complete for simulation number ${N}"
