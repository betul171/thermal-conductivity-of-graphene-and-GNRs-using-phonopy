from ase.io import read, write


atoms = read("graphene.dat", format="lammps-data")

atoms.center(axis=2) ### Center in z-direction to avoid interactions in z-direction.

write("POSCAR-unitcell", atoms, format="vasp")
