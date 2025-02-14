1. Create a lammps script to generate a lammps data file.

(main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??

2. Convert 'graphene.dat' to POSCAR format using a python script.

(main filename: lammps2poscar.py, generated filename: POSCAR-unitcell)

3. Write "phono3py -d --dim 2 2 2 --dim-fc2 4 4 4 --pa auto -c POSCAR-unitcell" on terminal.
   
   (generated filenames: phono3py_disp.yaml, POSCAR-00001...POSCAR-00372)

4. Create python script that converts POSCAR file to lammps data file.

(main filename: auto_poscar2lammps.py, generated filenames: POSCAR-*.dat)

5. Create a lammps script to extract forces.
(main filename: auto_extract_forces.py; used filenames: POSCAR-*.dat , generated filenames: forces_POSCAR- *.dump)

   
