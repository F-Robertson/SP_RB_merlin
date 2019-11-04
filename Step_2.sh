#! /bin/bash
#SBATCH -A spnmmd

In=$1
Out=$2
ped=$3

script_path="/nobackup/proj/spnmmd/NOV19/SIMULATION/ARRAY_SCRIPTS/"
#JobID1 = "array"

echo "${In} is the path"

echo ${SLURM_ARRAY_TASK_ID}

P=`awk "NR==$SLURM_ARRAY_TASK_ID" $In`

echo $P

no_of_lines=$(wc -l < $ped)

job2=$(sbatch --array=1-"${no_of_lines}"%100 ${script_path}/step_2_half.sh  "${P}" "${Out}" "${ped}")

#--jobname="${JobID1}" 