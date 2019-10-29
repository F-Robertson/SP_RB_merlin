#! /bin/bash
#SBATCH -A spnmmd


# run vis sbatch Launcher.sh /path/to/outfolder numberofsim 

Out=$1
N=$2

script_path="/mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS"
pheno_path="/mnt/storage/nobackup/proj/spnmmd/OCT19/SIMULATION/FILES.txt"
ped_path="${Out}/Paths_to_peds.txt"

JobID1="run_Sim"
JobID2="pathfinder"
JobID3="Run_Analysis"

#running the simulations
job1=$(sbatch --job-name="${JobID1}" --array=1-"${N}"%100 ${script_path}/Step_1.sh "${Out}")

echo $job1 &
wait $job1

#find paths to simulations and writing to a file
job2=$(sbatch --dependency=aftercorr:$job1 --job-name="${JobID2}" ${script_path}/paths_ped.sh "${Out}")

echo $job2

#setting up the pheno array
no_of_lines=$(wc -l < $pheno_path)

job3=$(sbatch --dependency=aftercorr:$job2 --job-name="${JobID3}" --array=1-"${no_of_lines}"%20 ${script_path}/Step_2.sh "${pheno_path}" "${Out}" "${ped_path}")

echo $job3



echo "i think i am done"