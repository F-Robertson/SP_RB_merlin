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

# THE SCRIPT STARTS HERE 
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def parse_command_line():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        '-o',
        help = 'Path to out folder',
        dest = 'OUT_Folder',
        required = True
    )
    options = parser.parse_args()
    return options

args = parse_command_line()

# set arguments as variables 
Folder_out=args.OUT_Folder #our path to outfolder where we want all the simulation going 

Sim_folder = make_out_dir(Folder_out,"Sims")

#suffixes
ped=".ped"

ped_files = []

for f in os.listdir(Sim_folder):
    if f.endswith(ped):
        F_path= Path(Sim_folder,f)
        ped_files.append(F_path)
    else:
        continue

path_filename = 'Paths_to_peds.txt'
fastq_path = Path(Folder_out,path_filename)

with open(str(fastq_path), 'a', newline='') as paths_text:
    for folder in ped_files:
        paths_text.write(str(folder)+'\n')
paths_text.close()

