# extract frequency data from band.yaml
import yaml

# Load the band.yaml file
with open('band.yaml', 'r') as f:
    band_data = yaml.safe_load(f)

# Extract the phonon frequencies
phonon_data = band_data['phonon']

# Loop through the phonon data to extract frequencies
for i, phonon in enumerate(phonon_data):
    q_position = phonon['q-position']
    print(f'Phonon {i + 1} at q-position {q_position}:')

    # Extract frequencies from the band list
    for band in phonon['band']:
        frequency = band['frequency']
        print(f'  Frequency: {frequency} THz')  # Adjust units if needed
    print()  # Blank line between phonons for clarity
