#Import things we will need
import pyrosetta
from pyrosetta import rosetta


#Function that does the ironically named "FastRelax"
#Param -- Cleaned PDB PATH
def fast_relax(pdb_path):

    #The new path will be the cleaned pdb + _Relaxed
    output_pdb_path = pdb_path.replace('.pdb', '_Relaxed.pdb')

    #Print statements to keep user updated
    print("Initializing PyRosetta...")
    
    #Initialize and tell it to quit yapping
    pyrosetta.init(extra_options="-mute all -constant_seed")
    print("PyRosetta initialized.")

    print(f"Loading PDB file: {pdb_path}")
    #Put the Cleaned PDB into a Pose
    pose = rosetta.core.import_pose.pose_from_file(pdb_path)
    print("PDB file loaded.")

    print("Applying FastRelax protocol...")
    # set the Relax as the Known Fast Relax Method from the protocols
    relax = rosetta.protocols.relax.FastRelax()
    #Score the relax using ref2015_cart cartesian is better for DDG I think.... Change if not
    relax.set_scorefxn(rosetta.core.scoring.ScoreFunctionFactory.create_score_function("ref2015_cart"))
    #Do the thing
    relax.apply(pose)
    #say Did the thing
    print("FastRelax protocol applied.")

    # Save the relaxed pose
    pose.dump_pdb(output_pdb_path)
    print(f"Relaxed pose saved to '{output_pdb_path}'.")





# INPUT SECTION
#Only INPUT path to "Cleaned" but not relaxed PDB here Within parentheses --> "PATH"
pdb_path = "/Users/shayneskrtic/Desktop/6k9j.clean.pdb"  
fast_relax(pdb_path)
