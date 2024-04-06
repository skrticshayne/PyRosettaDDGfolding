import pyrosetta
from pyrosetta.toolbox import cleanATOM

def clean_pdb_with_cleanATOM(pdb_path):
    # Initialize PyRosetta
    pyrosetta.init(extra_options="-mute all")

    # Define the output file name
    cleaned_pdb_path = pdb_path.replace('.pdb', '_cleaned.pdb')
    
    # Use PyRosetta's cleanATOM to clean the PDB file
    cleanATOM(pdb_path)
    
    print(f"Cleaned PDB file saved as: {cleaned_pdb_path}")

# Example usage
pdb_path = "/Users/shayneskrtic/Desktop/6k9j.pdb"  # Specify your PDB file path
clean_pdb_with_cleanATOM(pdb_path)
