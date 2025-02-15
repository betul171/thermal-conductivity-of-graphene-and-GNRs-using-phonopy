1. Create a lammps script to generate a lammps data file.

(main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??

2. Convert 'graphene.dat' to POSCAR format using a python script.

(main filename: lammps2poscar.py, generated filename: POSCAR-unitcell)

3. Write "phono3py -d --dim 2 2 1 --dim-fc2 4 4 1 --pa auto -c POSCAR-unitcell" on terminal.
   
   (generated filenames: phono3py_disp.yaml, POSCAR-00001...POSCAR-00372)

4. Add "calculator: lammps" after "phono3py:" in phono3py_disp.yaml

First two lines of phono3py_disp.yaml is must be as below.


            
     phono3py:
   
        calculator: lammps
  
  


5. Create python script that converts POSCAR file to lammps data file.

(main filename: auto_poscar2lammps.py, generated filenames: POSCAR-*.dat)

6. Create a lammps script to extract forces.
   
(main filename: auto_extract_forces.py; used filenames: POSCAR-*.dat , generated filenames: forces_POSCAR- *.dump)

7. Create a python script that writes all 'forces_POSCAR-*.dump' filenames in a file.
   
   (main filename: generate_file_list.py, generated filename: file_list.dat)

8. To create 'FORCES_FC3' file, write "phono3py --cf3-file file_list.dat" on terminal.
   
   (generated filename: FORCES_FC3)

9. To create 'FORCE_SETS' file, write "phono3py --cfs" on terminal.
    <this command creates FORCE_SETS from FORCES_FC3>

    (generated filename: FORCE_SETS)

10. To create 'FORCES_FC2' file, write "phono3py --fs2f2" on terminal.
     <this command creates FORCES_FC2 from FORCE_SETS>

    (generated filename: FORCES_FC2)
    
   


   
