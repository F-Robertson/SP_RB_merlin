#!/bin/python3.6


# This is running the simulation once for X in array

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


def run_merlin(out_file,prefix,G_ped,G_dat,m_txt,sim_log,sim_err):

    cmd = ['merlin',
    '-p',
    str(G_ped),
    '-d',
    str(G_dat),
    '-m',
    str(m_txt),
    '--simulate --save --prefix',
    str(out_file)+str(prefix) 
    ]
    
    full_path=' '.join(cmd)

    subprocess.call(full_path,
    shell=True,
    stdout=sim_log,
    stderr=sim_err
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

# THE SCRIPT STARTS HERE 
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#read in from commandline

def parse_command_line():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '-o',
        help = 'Path to out folder',
        dest = 'OUT_Folder',
        required = True
    )
    parser.add_argument(
        '-n',
        help = 'Number of simulations to run',
        dest = 'count_no',
        required = True
    )


    options = parser.parse_args()
    return options

args = parse_command_line()

# set arguments as variables 
Folder_in=Path("/nobackup/proj/spnmmd/OCT19/SIMULATION/") #hardcoded location of geno.ped/geno.dat/map.txt
Folder_out=args.OUT_Folder #our path to outfolder where we want all the simulation going 

No_sim=args.count_no

#make log folder

Log_folder_make= make_out_dir(Folder_out,"Sim_Logs")
Log_folder = Path(Log_folder_make)
Sim_folder_make = make_out_dir(Folder_out,"Sims")
Sim_folder=Path(Sim_folder_make)

#Location of three in files

G_ped= Path(Folder_in,"GENOS.ped")
G_dat= Path(Folder_in,"GENOS.dat")
m_txt= Path(Folder_in,"MAP.txt")


prefix="rep_no_"+str(No_sim)


Sim_logger=Logger("sim"+str(No_sim),Path(Log_folder))
Sim_logger.open()

run_merlin(Sim_folder,prefix,G_ped,G_dat,m_txt,Sim_logger.log_file,Sim_logger.err_file)










