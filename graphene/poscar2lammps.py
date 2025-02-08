from ase.io import read, write

poscar_file = "POSCAR-001"
atoms = read(poscar_file, format="vasp")

# Write the LAMMPS data file
lammps_data_file = "POSCAR-001.dat"
write(lammps_data_file, atoms, format="lammps-data")
print(f"Converted {poscar_file} to {lammps_data_file}")
