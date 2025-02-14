# Create force data with LAMMPS.
# There is no need to run dynamics. We are only interested to create force data files.
### NOTE: Since I want to get only the initial configuration, I do not minimize the system.

from lammps import lammps

lmp = lammps()

command = """
units metal
dimension 3
boundary p p p 
atom_style atomic

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

region graphene_box block 0 1 0 1 -0.25 0.25 units lattice

create_box 1 graphene_box
create_atoms 1 region graphene_box

mass 1 12.011 

pair_style airebo 3.0
pair_coeff * * CH.airebo C

write_data graphene.dat
"""

lmp.commands_string(command)

lmp.close()
