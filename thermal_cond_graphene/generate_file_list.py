fID = open("file_list.dat", "w")

for i in range(1, 189):
    fID.write(f"forces_POSCAR-{i:05d}.dump\n")

fID.close()
