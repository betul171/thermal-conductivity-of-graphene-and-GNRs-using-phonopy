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

# ---------- Read the Supercell Data ---------------------
read_data POSCAR_old-002.dat    # Don't forget to update POSCAR_old-002.data 

# ---------- Define Interatomic Potential ---------------------
pair_style airebo 3.0           
pair_coeff * * CH.airebo C 

# ---------- Set Atomic Mass ---------------------
mass 1 12.011  # Atomic mass of carbon for type 1

# ---------- Compute Forces ---------------------
compute myforces all property/atom fx fy fz  
dump 1 all custom 1 forces_POSCAR-002.dump id type x y z fx fy fz  # Don't forget to update POSCAR_old-002.data 

# ---------- Run the Simulation ---------------------
run 0                        


"""

lmp.commands_string(command)

lmp.close()
