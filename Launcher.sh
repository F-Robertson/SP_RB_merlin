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
job1=$(sbatch --parsable --job-name="${JobID1}" --array=1-"${N}"%100 ${script_path}/Step_1.sh "${Out}")
sleep 2
echo ${job1} 
j1=${job1} 

sbatch --job-name=run_Sim --array=1-3%100 /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Step_1.sh /nobackup/proj/spnmmd/OCT19/SIMULATION/TEST_OUT

#find paths to simulations and writing to a file
job2=$(sbatch --parsable --dependency=afterok::$j1 --job-name="${JobID2}" ${script_path}/paths_ped.sh "${Out}")
sleep 2
echo ${job2}
j2=${job2} 

#setting up the pheno array
no_of_lines=$(wc -l < $pheno_path)

job3=$(sbatch --parsable --dependency=aftercorr:$j2 --job-name="${JobID3}" --array=1-"${no_of_lines}"%20 ${script_path}/Step_2.sh "${pheno_path}" "${Out}" "${ped_path}")
sleep 2
echo ${job3}

echo "We Have Liftoff!!!!"
