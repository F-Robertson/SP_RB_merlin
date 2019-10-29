#!/bin/python3.6

#############################################
# Load python libraries
#############################################
import pathlib, subprocess, os, re, argparse
from pathlib import Path

#############################################
# functions
#############################################

def make_out_dir(outfolder,dir_name):
    directory = Path(outfolder,dir_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

#get sample IDs 
def get_sampleID(file_name, suffix):
    
    sample_name_in = re.sub(suffix, "", file_name)
    sample_id = sample_name_in
    return sample_id

def run_analysis(P_ped,S_ped,P_dat,S_dat,m_file,out_path,sample_id,A_log,A_err):

    cmd=["merlin",
    '-p',
    str(P_ped)+','+str(S_ped),
    '-d',
    str(P_dat)+','+str(S_dat),
    '-m',
    str(m_file),
    '--vc',
    '--markerNames',
    '--useCovariates',
    '--tabulate',
    '--prefix',
    str(out_path)+str(sample_id)
    ]

    full_path=' '.join(cmd)

    subprocess.call(full_path,
    shell=True,
    stdout=A_log,
    stderr=A_err
    )

#############################################
# classes
#############################################
class Logger:

    # Sets up the class for creating paths to log files - set up by variable=Logger()
    def __init__(self, task_name, folder_path):

        self.task_name = task_name
        self.folder_path = folder_path

    # For opening the log files - set up needs to be run to create Logger called by variable.open()
    def open(self,):
        self.log_file = open(Path(self.folder_path, self.task_name + '_log.txt'), 'w')
        self.err_file = open(Path(self.folder_path, self.task_name + '_err.txt'), 'w')

#telling python what each cmd line arg is

def parse_command_line():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '-o',
        help = 'Path to out folder',
        dest = 'OUT_Folder',
        required = True
    )
    parser.add_argument(
        '-p',
        help = 'path to pheno folder',
        dest = 'pheno',
        required = True
    )
    parser.add_argument(
        '-s',
        help = 'path to ped folder',
        dest = 'sim',
        required = True
    )
    
    options = parser.parse_args()
    return options

args = parse_command_line()


#reading folders into variables from cmd line
pheno_folder = args.pheno
Folder_out = args.OUT_Folder
Sim_file =args.sim

Map_file = Path("/nobackup/proj/spnmmd/OCT19/SIMULATION/MAP.txt")
Log_folder_make = make_out_dir(Folder_out,"Analysis_Logs")
Log_folder=Path(Log_folder_make)


#suffixes
ped_suff=".ped"
dat_suff=".dat"

#path to simulated files
#ped
sim_ped = Path(Sim_file)
#dat
sim_path = os.path.dirname(Sim_file)
samp_id = get_sampleID(Sim_file,ped_suff)
dat_name = samp_id+dat_suff
sim_dat=Path(sim_path,dat_name)

pheno_name = os.path.basename(pheno_folder)


for file_in in pheno_folder:
    if file_in.endswith(ped_suff):
        pheno_ped=Path(pheno_folder,file_in)

    elif file_in.endswith(dat_suff):
        pheno_dat=Path(pheno_folder,file_in)
    else:
        continue

New_out=Path(Folder_out,pheno_name)
out_path=Path(New_out,samp_id)

full_name=str(pheno_name)+"_"+str(samp_id)

Analysis_Log=Logger(full_name,Log_folder)
Analysis_Log.open()

run_analysis(pheno_ped,sim_ped,pheno_dat,sim_dat,Map_file,out_path,samp_id,Analysis_Log.log_file,Analysis_Log.err_file)





