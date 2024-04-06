# PyRosettaDDGfolding
This Directory contains three Scripts used by the Escorcia Lab at Xavier University to predict the DDG upon mutation of a SNP mutation. These scripts were adapted from freely available PyRosetta Scripts. 

# Cleaner.py
This script takes a PDB file and cleans it for use with PyRosetta

# Relaxer.py 
This script takes a cleaned PDB as Input and does a "FastRelax" Protocol on it (Highly recomended before performing a mutation)

# DDG_Calculator.py
This script takes the cleaned and Relaxed PDB and an AA mutation position and 1 Letter Code of the variant AA.

# Notes
This script can easily be adapted for Mutagenesis Runs by adding all 20 AA in the Array of Variant AA's
