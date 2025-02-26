#!/bin/zsh

### I am trying to find a way to stop excessive memory usage.

# Function to count the number of POSCAR files
count_poscars() {
    ls POSCAR-* 2>/dev/null | wc -l
}

# Run phono3py in the background to generate files
phono3py -d --dim 2 2 1 -c POSCAR-unitcell --pa auto & # use & to run phono3py on the background
PHONO_PID=$!  # Capture the PID of phono3py

# Loop until 10 or more POSCAR files are generated
while true; do
    # Check the number of POSCAR files
    file_count=$(count_poscars)

    # If we have 10 or more files, stop phono3py
    if [ "$file_count" -ge 10 ]; then
        echo "10 or more POSCAR files generated ($file_count). Stopping phono3py."
        kill "$PHONO_PID" 2>/dev/null
        break
    fi

    # Sleep for 1 second before checking again
done

# Force stop in case it's still running
kill "$PHONO_PID" 2>/dev/null
wait "$PHONO_PID" 2>/dev/null
