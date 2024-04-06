import pyrosetta
from pyrosetta import rosetta

def fast_relax(pdb_path, output_pdb_path):
    print("Initializing PyRosetta...")
    pyrosetta.init(extra_options="-mute all -constant_seed")
    print("PyRosetta initialized.")

    print(f"Loading PDB file: {pdb_path}")
    pose = rosetta.core.import_pose.pose_from_file(pdb_path)
    print("PDB file loaded.")

    print("Applying FastRelax protocol...")
    relax = rosetta.protocols.relax.FastRelax()
    relax.set_scorefxn(rosetta.core.scoring.ScoreFunctionFactory.create_score_function("ref2015_cart"))
    relax.apply(pose)
    print("FastRelax protocol applied.")

    # Save the relaxed pose
    pose.dump_pdb(output_pdb_path)
    print(f"Relaxed pose saved to '{output_pdb_path}'.")

# Example usage
pdb_path = "/Users/shayneskrtic/Desktop/mutant_P_1.pdb"  # Path to your PDB file
output_pdb_path = "/Users/shayneskrtic/Desktop/2xxxrelaxed_structure.pdb"  # Output path for the relaxed structure
fast_relax(pdb_path, output_pdb_path)
