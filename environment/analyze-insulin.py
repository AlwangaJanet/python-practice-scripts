# Open the file containing the raw sequence
with open('preproinsulin-seq.txt', 'r') as f:
    raw_sequence = f.read()

# Clean the sequence by removing "ORIGIN", numbers, spaces, and "//"
cleaned_sequence = ''.join([line.strip() for line in raw_sequence.splitlines() if not line.startswith('ORIGIN') and not line.startswith('//') and not line.isdigit()])
cleaned_sequence = cleaned_sequence.replace(" ", "")

# Save the cleaned sequence
with open('preproinsulin-seq-clean.txt', 'w') as f:
    f.write(cleaned_sequence)

# Check the length of the cleaned sequence
print(f"The cleaned sequence has {len(cleaned_sequence)} characters.")

# Extract the different parts of the sequence
lsinsulin_seq = cleaned_sequence[0:24]   # Amino acids 1-24
binsulin_seq = cleaned_sequence[24:54]   # Amino acids 25-54
cinsulin_seq = cleaned_sequence[54:89]   # Amino acids 55-89
ainsulin_seq = cleaned_sequence[89:110]  # Amino acids 90-110

# Save each part into its own file
with open('lsinsulin-seq-clean.txt', 'w') as f:
    f.write(lsinsulin_seq)

with open('binsulin-seq-clean.txt', 'w') as f:
    f.write(binsulin_seq)

with open('cinsulin-seq-clean.txt', 'w') as f:
    f.write(cinsulin_seq)

with open('ainsulin-seq-clean.txt', 'w') as f:
    f.write(ainsulin_seq)

# Verify lengths of each part
print(f"lsinsulin sequence has {len(lsinsulin_seq)} characters.")
print(f"binsulin sequence has {len(binsulin_seq)} characters.")
print(f"cinsulin sequence has {len(cinsulin_seq)} characters.")
print(f"ainsulin sequence has {len(ainsulin_seq)} characters.")

