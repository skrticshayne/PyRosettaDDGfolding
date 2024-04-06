#Import Neccesities 
from pyrosetta import *
from pyrosetta.rosetta import *
from pyrosetta.toolbox import *
from pyrosetta.teaching import *

#Initialize With Optimizations to ignore anything unrecognized that may have slipped through cleaning 
#Cartesian Relaxing 
init("-ignore_unrecognized_res 1 -ex1 -ex2 -flip_HNQ -relax:cartesian -nstruct 200 -crystal_refine -optimization:default_max_cycles 200")






# INPUT SECTION
#Only INPUT path to "Cleaned and Relaxed" PDB here Within parentheses --> "PATH"
testPose = pose_from_pdb("/Users/shayneskrtic/Desktop/6k9j.clean_Relaxed.pdb")





#Set the score type- Standard
scorefxnDDG = get_fa_scorefxn()

# Record the initial score of the already relaxed structure
#this will be used to calc DDG
s0 = scorefxnDDG(testPose)

# Energy minimization  setup
min_mover = rosetta.protocols.minimization_packing.MinMover()  # define a Mover in type of MinMover

#Initializations for Movers
mm = MoveMap()
mm.set_bb_true_range(28, 36)
min_mover.movemap(mm)
#Score with our score we defined
min_mover.score_function(scorefxnDDG)

#Literature sugges .01 here seems to not make huge difference in output of MC
min_mover.tolerance(0.01)

#output for user
print(min_mover)


#array to hold our DDG Values 
#allows for Mutagenesis
ddG = []


#minimize energy using MC Simulation param - the pose of the pdb 
def minimize_Energy(pose):
    # Minimization
    min_mover.apply(pose)

    # Trial_mover define
    #Kt normal at 1 adjust if you want a different kT This is usually higher at high heats ~1 = ~ physiological 
    kT = 1.0

    # make mc a monteCarlo with our scoring and our Kt
    mc = MonteCarlo(pose, scorefxnDDG, kT)
    mc.boltzmann(pose)
    mc.recover_low(pose)

    #setup needed for MC
    trial_mover = TrialMover(min_mover, mc)
    #Run Monte Carlo
    #iteartions set to 100 as of now change if results necessitate 
    for i in range(100):
        trial_mover.apply(pose)


# Point mutation
#comma seperated for more(mnutagenesis) Adjust this line fot the AA You want to Change
AA = ['G']
mp = Pose()
for index, i in enumerate(AA, start=1):
    mp.assign(testPose)
    #CHANGE THIS LINE FOR POSITION OF MUTATION ONLY CHANGE NUMBER 
    #MAKE SURE THIS MATCHES THE POSITION IN THE SEQUENCE OF THE MUTATION
    mutate_residue(mp, 8, i)
    minimize_Energy(mp)
    

    #FINAL Score - INITIAL score = CHANGE ... + = destabilizing and - = stabilizing

    s1 = scorefxnDDG(mp)
    dg = s1 - s0
    ddG.append(dg)


# Output numbers
print("The energy after initial scoring: ", s0)
print("The ddG: ")
print(ddG)
