1. Create a lammps script to generate a lammps data file.
   (main filename: create_lammps_data.py, generated filename: graphene.dat) SLANTED??
   
3. Convert 'graphene.dat' to POSCAR format using a python script.
  (main filename: lammps2poscar.py, generated filename: POSCAR) 
      
4. Write 'phonopy --dim="4 2 1" -d --amplitude=0.01' on terminal to create displaced POSCAR files.
   (generated filenames:POSCAR-001, POSCAR-002, phonopy_disp.yaml)
   
5. Create python script that converts POSCAR file to lammps data file. Run POSCAR-001 and POSCAR-002 seperately.
    (main filename: poscar2lammps.py, generated filenames: POSCAR-001.dat, POSCAR-002.dat).
   
6. Create a lammps script to extract forces.
     (main filename: extract_forces.py; used filenames: POSCAR-001.dat, POSCAR-002.dat; generated filenames: forces_POSCAR-001.dump, forces_POSCAR-002.dump)

7. Write "phonopy --lammps -f forces_POSCAR-*.dump" on terminal.
    (generated filename: FORCE_SETS)  
   
8. Write 'phonopy --band="0 0 0  0.5 0 0  1/3 1/3 0  0 0 0" -c phonopy_disp.yaml' OR 'phonopy --band="0 0 0  0.5 0 0  1/3 1/3 0  0 0 0"' on terminal to generate 'band.yaml'
    (generated filename: band.yaml, phonon.yml)

9. An alternative to 9: Create a file named band.conf. Then write "phonopy --band -c phonopy_disp.yaml -d band.conf" on terminal. (This item do not work!)

10. Analize the data.
    
    to see phonon dispersion curve: "phonopy -p band.conf"
    If you want phonon frequencies at a specific q-point: phonopy --qpoints="0 0 0"
    If you have multiple q-points, create a file qpoints.conf, and use: phonopy --qpoints qpoints.conf
    

