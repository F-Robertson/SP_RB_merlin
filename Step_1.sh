#! /bin/bash
#SBATCH -A spnmmd


# This runs the simulation for the number passed by array ID

module load merlin
module load Python/3.6.6-intel-2018b

Out=$1

echo ${SLURM_ARRAY_TASK_ID}

N=${SLURM_ARRAY_TASK_ID}

python3.6 /nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Py_scripts/step_1.py -o ${Out} -n ${N}

wait

echo "Complete for simulation number ${N}"
