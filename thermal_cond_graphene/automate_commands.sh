#!/bin/zsh

#### Adjust the code. I did not check whether this script works well.


# Step 1: Generate the LAMMPS data file using create_lammps_data.py
python3 create_lammps_data.py

# Step 2: Convert 'graphene.dat' to POSCAR format using lammps2poscar.py
python3 lammps2poscar.py

# Step 3: Run phono3py to create displacement files
phono3py -d --dim 2 2 1 -c POSCAR-unitcell

# Step 4: Modify phono3py_disp.yaml to include 'calculator: lammps'
sed -i '2i\    calculator: lammps' phono3py_disp.yaml

# Step 5: Convert POSCAR files to LAMMPS data files using auto_poscar2lammps.py
python3 auto_poscar2lammps.py

# Step 6: Extract forces using auto_extract_forces.py
python3 auto_extract_forces.py

# Step 7: Generate a file list of 'forces_POSCAR-*.dump' filenames
python3 generate_file_list.py

# Step 8: Create 'FORCES_FC3' file using phono3py
phono3py --cf3-file file_list.dat

## Step 9 & 10 are optional.

# Step 11: Create fc3.hdf5 and fc2.hdf5 files using phono3py-load
phono3py-load

# Step 12: Calculate lattice thermal conductivity using 11x11x11 sampling mesh
phono3py-load --mesh 11 11 11 --br

# Step 13: Calculate accumulated lattice thermal conductivity
phono3py-kaccum kappa-m111111.hdf5 | tee kaccum.dat
