#! /bin/bash
#SBATCH -A spnmmd

In=$1
Out=$2
ped=$3

script_path="/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/"
JobID1 = "Not_DROIDS"

echo "${In} is the path"

echo ${SLURM_ARRAY_TASK_ID}

P=`awk "NR==$SLURM_ARRAY_TASK_ID" $In`

echo $P

no_of_lines=$(wc -l < $ped)

job2ish= $(sbatch --jobname="${JobID1}" --array=1-"${no_of_lines}"%100 ${script_path}/step_2_half.sh  "${P}" "${Out}" "${ped}")