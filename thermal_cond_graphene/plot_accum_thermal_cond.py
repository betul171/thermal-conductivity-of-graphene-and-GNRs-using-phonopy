# Plot accumulated thermal conductivity.
# This code is not mine and generated  by ChatGPT.

import numpy as np
import matplotlib.pyplot as plt

# Function to read a specific block of data from the file
def read_block(filename, block_index):
    data = []
    with open(filename, 'r') as file:
        current_block = 0
        block_data = []
        for line in file:
            if line.startswith('#'):  # Skip comment lines
                continue
            if line.strip() == '':  # Blank line indicates end of a block
                if block_data:
                    if current_block == block_index:
                        data = np.array(block_data)
                        break
                    block_data = []  # Reset for the next block
                    current_block += 1
            else:
                block_data.append([float(x) for x in line.split()])
    return data

# File name and block index (30th block)
filename = 'kaccum.dat'
block_index = 29

# Read the 30th block
data = read_block(filename, block_index)

# Check if the data is available
if data.size > 0:
    data = np.array(data)  # Convert the data to a NumPy array

    # Extract columns 1 and 2 (index 0 and 1)
    x = data[:, 0]
    y = data[:, 1]

    # Plot the data
    plt.plot(x, y)
    plt.xlabel('Frequency(THz)')
    plt.ylabel('Accumulated kappa (W / m·K)')
    plt.title(f' Frequency(THz) vs Accumulated Kappa at 300K')
    #plt.legend()
    plt.grid(True)
    plt.show()
else:
    print(f"No data found in block {block_index}.")
