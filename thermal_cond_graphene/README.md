## The aim of this directory is to calculate thermal conductivity of graphene piece containing 4 atoms using phono3py and LAMMPS.

1. Create a lammps script to generate a lammps data file.
   
   (main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??
   
2. Convert 'graphene.dat' to POSCAR format using a python script.

   (main filename: lammps2poscar.py, generated filename: POSCAR)

3. Write 'phono3py --dim="4 2 1" -d --amplitude=0.01' on terminal to create displaced POSCAR files.

   (generated filenames:POSCAR-* <POSCAR-0001, POSCAR-0002, etc.>, phono3py_disp.yaml)

4. Create python script that converts POSCAR file to lammps data file.

(main filename: auto_poscar2lammps.py, generated filenames: POSCAR-*.dat).

5. Create a lammps script to extract forces.

(main filename: auto_extract_forces.py; used filenames: POSCAR-*.dat , generated filenames: forces_POSCAR- *.dump)


################################# new try ##########################################
phono3py -d --dim 1 1 1 --dim-fc2 1 1 1 --pa auto -c POSCAR-unitcell
extract forces as usual
phonopy -c POSCAR-unitcell -d --dim 1 1 1 etc. with phonopy create FORCE_SETS file in another directory.
move FORCE_SETS file to current directory
phono3py --fs2f2 creates FORCES_FC2



