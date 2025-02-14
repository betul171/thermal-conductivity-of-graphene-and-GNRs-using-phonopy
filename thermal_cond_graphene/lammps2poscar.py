from ase.io import read, write

# Read the LAMMPS data file
atoms = read("graphene.dat", format="lammps-data")

# Write to POSCAR_old format
write("POSCAR-unitcell", atoms, format="vasp")
