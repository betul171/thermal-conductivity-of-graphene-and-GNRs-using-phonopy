import h5py

# Open the HDF5 file
f = h5py.File("kappa-m111111.hdf5", "r")

temperatures = f["temperature"][:]  # Read temperature values
kappa = f["kappa"][:]  # Read thermal conductivity tensor

f.close()


# Find the index corresponding to 300 K
if 300 in temperatures:
    index_300K = list(temperatures).index(300)
    kappa_300K = kappa[index_300K]
    print(f"Lattice Thermal Conductivity at 300 K: {kappa_300K} W/mK")
else:
    print("300 K data not found in the file.")
