
#!/bin/python3.6


import commands, os

script_path="/mnt/storage/nobackup/proj/rtmngs/testing_cp"
JobID1="one_1"
JobID2="one_2"
JobID3="one_3"

# submit the first job
cmd = "sbatch --job-name=one_1 /mnt/storage/nobackup/proj/rtmngs/testing_cp/test_1.sh"
print("Submitting Job1 with command: %s" % cmd)
status, jobnum = commands.getstatusoutput(cmd)
if (status == 0 ):
    print("Job1 is %s" % jobnum)
else:
    print("Error submitting Job1")

# submit the second job to be dependent on the first
cmd = "sbatch --dependency=afterok:%s --job-name=one_2 /mnt/storage/nobackup/proj/rtmngs/testing_cp/test_2.sh" % jobnum
print ("Submitting Job2 with command: %s" % cmd)
status,jobnum = commands.getstatusoutput(cmd)
if (status == 0 ):
    print ("Job2 is %s" % jobnum)
else:
    print ("Error submitting Job2")

# submit the third job (a swarm) to be dependent on the second
cmd = "sbatch --depend=afterok:%s --job-name=one_3 /mnt/storage/nobackup/proj/rtmngs/testing_cp/test_3.sh" % jobnum
print ("Submitting swarm job  with command: %s" % cmd)
status,jobnum = commands.getstatusoutput(cmd)
if (status == 0 ):
    print ("Job3 is %s" % jobnum)
else:
    print ("Error submitting Job3")