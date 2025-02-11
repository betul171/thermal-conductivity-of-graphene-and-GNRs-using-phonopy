import os
from ase.io import read, write

# Get all POSCAR-* files in the current directory
poscar_files = sorted([f for f in os.listdir() if f.startswith("POSCAR-")])

# Loop through each POSCAR-* file
for poscar_file in poscar_files:
    try:
        # Read the POSCAR file
        atoms = read(poscar_file, format="vasp")

        # Define the output LAMMPS data file name
        lammps_data_file = poscar_file + ".dat"

        # Write the LAMMPS data file
        write(lammps_data_file, atoms, format="lammps-data")

        print(f"Converted {poscar_file} -> {lammps_data_file}")

    except Exception as e:
        print(f"Error processing {poscar_file}: {e}")
