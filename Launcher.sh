

# Anything that is in "" needs replaced before running
#running the simulations
job1= 
sbatch --job-name=run_Sim --array=1-"N"%100 /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Step_1.sh "OUT"

sbatch --job-name=run_Sim --array=1-3%100 /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Step_1.sh /nobackup/proj/spnmmd/OCT19/SIMULATION/TEST_OUT

#find paths to simulations and writing to a file
job2= 
sbatch --dependency=afterok:$"j1" --job-name=pathfinder /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/paths_ped.sh "Out"

sbatch --dependency=afterok:892441 --job-name=pathfinder /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/paths_ped.sh /nobackup/proj/spnmmd/OCT19/SIMULATION/TEST_OUT

job3= 
sbatch --dependency=afterok:$"job2" --job-name=Run_Analysis --array=1-"no_of_lines"%20 /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Step_2.sh /mnt/storage/nobackup/proj/spnmmd/OCT19/SIMULATION/FILES.txt "Out" "Out"/Paths_to_peds.txt

sbatch --dependency=afterok:892445 --job-name=Run_Analysis --array=1-3%20 /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Step_2.sh /mnt/storage/nobackup/proj/spnmmd/OCT19/SIMULATION/FILES.txt /nobackup/proj/spnmmd/OCT19/SIMULATION/TEST_OUT /nobackup/proj/spnmmd/OCT19/SIMULATION/TEST_OUT/Paths_to_peds.txt