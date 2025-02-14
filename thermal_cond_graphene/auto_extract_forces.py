# Create force data with LAMMPS.
# There is no need to run dynamics. We are only interested to create force data files.
## Since we are performing finite displacement calculations (which Phono3py uses), we want forces from slightly displaced configurations, not a fully minimized one.
import os
from lammps import lammps

# Get all LAMMPS data files (e.g., POSCAR-001.dat, POSCAR-002.dat, etc.)
data_files = sorted([f for f in os.listdir() if f.startswith("POSCAR-") and f.endswith(".dat")])

# Loop through each data file and run LAMMPS
for data_file in data_files:
    # Extract the base name (e.g., "POSCAR-001" from "POSCAR-001.dat")
    base_name = data_file.replace(".dat", "")

    # Define the output force file
    force_dump_file = f"forces_{base_name}.dump"

    # Initialize LAMMPS
    lmp = lammps()

    # LAMMPS command script
    command = f"""
    # ---------- Initialize Simulation ---------------------
    units metal                  
    dimension 3                  
    boundary p p p               
    atom_style atomic            

    # ---------- Read the Supercell Data ---------------------
    read_data {data_file}    

    # ---------- Define Interatomic Potential ---------------------
    pair_style airebo 3.0           
    pair_coeff * * CH.airebo C 

    # ---------- Set Atomic Mass ---------------------
    mass 1 12.011  

    # ---------- Compute Forces ---------------------
    compute myforces all property/atom fx fy fz  
    dump 1 all custom 1 {force_dump_file} id type x y z fx fy fz  

    # ---------- Run the Simulation ---------------------
    run 0                        
    """

    # Run the LAMMPS commands
    print(f"Processing {data_file} -> {force_dump_file}")
    lmp.commands_string(command)

    # Close LAMMPS
    lmp.close()

print("All force calculations are complete.")
