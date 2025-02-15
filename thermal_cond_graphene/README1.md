1. Create a lammps script to generate a lammps data file.

(main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??

2. Convert 'graphene.dat' to POSCAR format using a python script.

(main filename: lammps2poscar.py, generated filename: POSCAR-unitcell)

3. Write "phono3py -d --dim 2 2 1 --dim-fc2 4 4 1 --pa auto -c POSCAR-unitcell" on terminal.
   
   (generated filenames: phono3py_disp.yaml, POSCAR-00001...POSCAR-00372)

4. Add "calculator: lammps" after "phono3py:" in phono3py_disp.yaml

Example first lines of phono3py_disp.yaml is below.

"""

phono3py:

  calculator: lammps
  
  version: "3.12.1"
  
"""

5. Create python script that converts POSCAR file to lammps data file.

(main filename: auto_poscar2lammps.py, generated filenames: POSCAR-*.dat)

6. Create a lammps script to extract forces.
   
(main filename: auto_extract_forces.py; used filenames: POSCAR-*.dat , generated filenames: forces_POSCAR- *.dump)

   
