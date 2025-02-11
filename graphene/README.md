### The aim of this directory is to calculate phonon frequencies of a graphene piece containing 4 atoms using phonopy and LAMMPS.

1. Create a lammps script to generate a lammps data file.
   
   (main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??
   
2. Convert 'graphene.dat' to POSCAR format using a python script.

   (main filename: lammps2poscar.py, generated filename: POSCAR) 
      
3. Write 'phonopy --dim="4 2 1" -d --amplitude=0.01' on terminal to create displaced POSCAR files.

   (generated filenames:POSCAR-001, POSCAR-002, phonopy_disp.yaml)
   
4. Create python script that converts POSCAR file to lammps data file. Run POSCAR-001 and POSCAR-002 seperately.
 
    (main filename: poscar2lammps.py, generated filenames: POSCAR-001.dat, POSCAR-002.dat).
   
5. Create a lammps script to extract forces.
 
     (main filename: extract_forces.py; used filenames: POSCAR-001.dat, POSCAR-002.dat; generated filenames: forces_POSCAR-001.dump, forces_POSCAR-002.dump)

6. Write "phonopy --lammps -f forces_POSCAR-*.dump" on terminal.
 
    (generated filename: FORCE_SETS)  
   
7. Write 'phonopy --band="0 0 0  0.5 0 0  1/3 1/3 0  0 0 0" -c phonopy_disp.yaml' OR 'phonopy --band="0 0 0  0.5 0 0  1/3 1/3 0  0 0 0"' on terminal to generate 'band.yaml'

    (generated filename: band.yaml, phonon.yml)

8. An alternative to 9: Create a file named band.conf. Then write "phonopy --band -c phonopy_disp.yaml -d band.conf" on terminal. (This item do not work!)

9. Analize the data.

    Phonon frequencies are extracted from 'band.yaml' with the file named 'extract_frequency_data.py'
    
    to see phonon dispersion curve:  "phonopy -p band.conf"
    
    If you want phonon frequencies at a specific q-point:  phonopy --qpoints="0 0 0"
    
    If you have multiple q-points, create a file qpoints.conf, and use:  phonopy --qpoints qpoints.conf
    

