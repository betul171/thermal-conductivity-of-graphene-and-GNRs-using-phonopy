1. Create a lammps script to generate a lammps data file.

(main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??

2. Convert 'graphene.dat' to POSCAR format using a python script.

(main filename: lammps2poscar.py, generated filename: POSCAR)

3. Write "phono3py -d --dim 2 2 2 --dim-fc2 4 4 4 --pa auto -c POSCAR-unitcell" on terminal.
