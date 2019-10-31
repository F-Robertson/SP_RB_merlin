


#running the simulations
job1= sbatch --job-name=run_Sim --array=1-"${N}"%100 /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Step_1.sh "${Out}"


#find paths to simulations and writing to a file
job2= sbatch --dependency=afterok:$j1 --job-name=pathfinder /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/paths_ped.sh "${Out}"



job3= sbatch --dependency=afterok:$job2 --job-name="Run_Analysis" --array=1-"${no_of_lines}"%20 /mnt/storage/nobackup/proj/spnmmd/OCT19/ARRAY_SCRIPTS/Step_2.sh "/mnt/storage/nobackup/proj/spnmmd/OCT19/SIMULATION/FILES.txt" "${Out}" ${Out}/Paths_to_peds.txt)

