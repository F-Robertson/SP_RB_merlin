#! /bin/bash
#SBATCH -A spnmmd

In=$1
Out=$2
ped=$3

module load merlin

echo "${In} is the path"

echo ${SLURM_ARRAY_TASK_ID}

Sim=`awk "NR==$SLURM_ARRAY_TASK_ID" $ped`

echo $Sim

python3.6 step_2.py -o ${Out} -p ${In} -s ${Sim}