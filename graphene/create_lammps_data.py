# Create force data with LAMMPS.
# This code is taken from Zeynep Altıntaş.
# There is no need to run dynamics. We are only interested to create force data files.
from lammps import lammps

lmp = lammps()

command = """

# ---------- Initialize Simulation ---------------------
units metal
dimension 3                
boundary p p p             
atom_style atomic

# ---------- Create Atoms ---------------------
variable a equal 1.42
variable z_spacing equal 10.0
variable a1x equal 3.0*${a}       
variable a2y equal sqrt(3)*${a}   

lattice custom 1.0 &
    a1 ${a1x} 0.0 0.0 &
    a2 0.0 ${a2y} 0.0 &
    a3 0.0 0.0 ${z_spacing} &
    basis 0.0 0.0 0.0 &
    basis 0.3333 0.0 0.0 &
    basis 0.5 0.5 0.0 &
    basis 0.8333 0.5 0.0

# Define a larger region with an extended z dimension
region graphene_box block 0 1 0 1 0 1 units lattice

create_box 1 graphene_box
create_atoms 1 region graphene_box

#dump 1 all custom 100 forces_*.lammpstrj id type fx fy fz

mass 1 12.011  # Mass of carbon in atomic mass units (amu)

# ---------- Interatomic Potential ---------------------
pair_style airebo 3.0           
pair_coeff * * CH.airebo C 

# ---------- Define Settings ---------------------
compute eng all pe/atom 
compute eatoms all reduce sum c_eng

write_data graphene.dat

# ---------- Run Minimization ---------------------
reset_timestep 0
fix 1 all box/relax aniso 0.0 vmax 0.001
thermo 10
thermo_style custom step pe lx ly lz press pxx pyy pzz c_eatoms
min_style cg
minimize 1e-25 1e-25 5000 10000

"""

lmp.commands_string(command)

lmp.close()
