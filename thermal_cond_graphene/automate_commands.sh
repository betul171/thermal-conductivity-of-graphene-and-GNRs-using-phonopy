#!/bin/bash

# Step 1: Generate the LAMMPS data file using create_lammps_data.py
echo "Step 1: Generating LAMMPS data file..."
python create_lammps_data.py
echo "LAMMPS data file 'graphene.dat' generated."

# Step 2: Convert 'graphene.dat' to POSCAR format using lammps2poscar.py
echo "Step 2: Converting 'graphene.dat' to POSCAR format..."
python lammps2poscar.py
echo "POSCAR file 'POSCAR-unitcell' generated."

# Step 3: Run phono3py to create displacement files
echo "Step 3: Running phono3py to generate displacement files..."
phono3py -d --dim 2 2 1 -c POSCAR-unitcell
echo "Displacement files generated (POSCAR-00001 to POSCAR-00188)."

# Alternative (you can uncomment the line below if needed)
# phono3py -d --dim 2 2 1 --dim-fc2 4 4 1 --pa auto -c POSCAR-unitcell

# Step 4: Modify phono3py_disp.yaml to include 'calculator: lammps'
echo "Step 4: Adding 'calculator: lammps' to phono3py_disp.yaml..."
sed -i '2i\    calculator: lammps' phono3py_disp.yaml
echo "'calculator: lammps' added to phono3py_disp.yaml."

# Step 5: Convert POSCAR files to LAMMPS data files using auto_poscar2lammps.py
echo "Step 5: Converting POSCAR files to LAMMPS data files..."
python auto_poscar2lammps.py
echo "LAMMPS data files 'POSCAR-*.dat' generated."

# Step 6: Extract forces using auto_extract_forces.py
echo "Step 6: Extracting forces from POSCAR-*.dat..."
python auto_extract_forces.py
echo "Forces extracted to 'forces_POSCAR-*.dump'."

# Step 7: Generate a file list of 'forces_POSCAR-*.dump' filenames
echo "Step 7: Generating file list of forces..."
python generate_file_list.py
echo "File list 'file_list.dat' generated."

# Step 8: Create 'FORCES_FC3' file using phono3py
echo "Step 8: Creating 'FORCES_FC3' using phono3py..."
phono3py --cf3-file file_list.dat
echo "'FORCES_FC3' file created."

# Step 9: (Optional) Create 'FORCE_SETS' file (not needed for thermal conductivity)
# echo "Step 9: Creating 'FORCE_SETS' using phono3py..."
# phono3py --cfs
# echo "'FORCE_SETS' file created."

# Step 10: (Optional) Create 'FORCES_FC2' file (not needed for thermal conductivity)
# echo "Step 10: Creating 'FORCES_FC2' using phono3py..."
# phono3py --fs2f2
# echo "'FORCES_FC2' file created."

# Step 11: Create fc3.hdf5 and fc2.hdf5 files using phono3py-load
echo "Step 11: Creating fc3.hdf5 and fc2.hdf5 files using phono3py-load..."
phono3py-load
echo "'fc3.hdf5' and 'fc2.hdf5' files created."

# Step 12: Calculate lattice thermal conductivity using 11x11x11 sampling mesh
echo "Step 12: Calculating lattice thermal conductivity using phono3py-load..."
phono3py-load --mesh 11 11 11 --br
echo "'kappa-m111111.hdf5' file created."

# Step 13: Calculate accumulated lattice thermal conductivity
echo "Step 13: Calculating accumulated lattice thermal conductivity using phono3py-kaccum..."
phono3py-kaccum kappa-m111111.hdf5 | tee kaccum.dat
echo "'kaccum.dat' file created."

# Step 14: Plot kaccum.dat using gnuplot
echo "Step 14: Plotting kaccum.dat using gnuplot..."
gnuplot -e "plot 'kaccum.dat' i 30 u 1:2 w l, 'kaccum.dat' i 30 u 1:8 w l"
echo "Plotting completed."

echo "Thermal conductivity calculation process completed!"
