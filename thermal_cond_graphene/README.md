## The aim of this directory is to calculate thermal conductivity of graphene piece containing 4 atoms using phono3py and LAMMPS.

1. Create a lammps script to generate a lammps data file.
   
   (main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??
   
2. Convert 'graphene.dat' to POSCAR format using a python script.

   (main filename: lammps2poscar.py, generated filename: POSCAR)

3. Write 'phono3py --dim="4 2 1" -d --amplitude=0.01' on terminal to create displaced POSCAR files.

   (generated filenames:POSCAR-*, phono3py_disp.yaml)

4. Create python script that converts POSCAR file to lammps data file. Run POSCAR-001 and POSCAR-002 seperately.

(main filename: poscar2lammps.py, generated filenames: POSCAR-001.dat, POSCAR-002.dat).

Create a lammps script to extract forces.

(main filename: extract_forces.py; used filenames: POSCAR-001.dat, POSCAR-002.dat; generated filenames: forces_POSCAR-001.dump, forces_POSCAR-002.dump)
