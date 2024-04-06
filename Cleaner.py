#import things we will need
import pyrosetta
from pyrosetta.toolbox import cleanATOM

#This is the Function that Cleans the PDB Remove water and return the new pdb path 


def clean_pdb_with_cleanATOM(pdb_path):
    # Initialize PyRosetta and make it stop Yapping
    pyrosetta.init(extra_options="-mute all")

    
    # Use PyRosetta's prebuilt cleaner function
    cleanATOM(pdb_path)

    #Print to let user Know it worked
    print(f"Cleaned PDB file saved as: Former pdb path .clean.pdb")






# INPUT SECTION
#Only INPUT path to "Dirty" PDB here Within parentheses --> "PATH"
pdb_path = "/Users/shayneskrtic/Desktop/6k9j.pdb"  

#run Script
clean_pdb_with_cleanATOM(pdb_path)
