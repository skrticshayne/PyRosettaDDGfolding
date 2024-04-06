from pyrosetta import *
from pyrosetta.rosetta import *
from pyrosetta.toolbox import *
from pyrosetta.teaching import *
init("-ignore_unrecognized_res 1 -ex1 -ex2 -flip_HNQ -relax:cartesian -nstruct 200 -crystal_refine -optimization:default_max_cycles 200")

# Parameter set up
testPose = pose_from_pdb("/Users/shayneskrtic/Desktop/2xrelaxed_structure.pdb")
scorefxnDDG = get_fa_scorefxn()

# Record the initial score of the already relaxed structure
s0 = scorefxnDDG(testPose)

# Energy minimization setup
min_mover = rosetta.protocols.minimization_packing.MinMover()  # define a Mover in type of MinMover
mm = MoveMap()
mm.set_bb_true_range(28, 36)
min_mover.movemap(mm)
min_mover.score_function(scorefxnDDG)
min_mover.tolerance(0.01)
print(min_mover)

ddG = []

def minimize_Energy(pose):
    # Minimization
    min_mover.apply(pose)

    # Trial_mover define
    kT = 1.0
    mc = MonteCarlo(pose, scorefxnDDG, kT)
    mc.boltzmann(pose)
    mc.recover_low(pose)

    trial_mover = TrialMover(min_mover, mc)
    # Monte Carlo
    for i in range(200):
        trial_mover.apply(pose)


# Point mutation
AA = ['G']
mp = Pose()
for index, i in enumerate(AA, start=1):
    mp.assign(testPose)
    mutate_residue(mp, 8, i)
    minimize_Energy(mp)
    
    s1 = scorefxnDDG(mp)
    dg = s1 - s0
    ddG.append(dg)

    # Save each mutated structure to a PDB file
   # pdb_filename = f"/Users/shayneskrtic/Desktop/mutant_{i}_{index}.pdb"  # Specify your save path here
   # mp.dump_pdb(pdb_filename)

# Output
print("The energy after initial scoring: ", s0)
print("The ddG: ")
print(ddG)
