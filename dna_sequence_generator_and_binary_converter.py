import random

def generate_random_dna_sequence(length):
    """Generate a random DNA sequence of a given length."""
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choice(bases) for _ in range(length))

def dna_to_binary(dna_sequence):
    """Convert a DNA sequence to a binary sequence."""
    base_to_binary = {'A': '00', 'T': '01', 'C': '10', 'G': '11'}
    return ''.join(base_to_binary[base] for base in dna_sequence)

# Generate a random DNA sequence
dna_sequence = generate_random_dna_sequence(100)  # Example length of 100

# Convert DNA sequence to binary
binary_sequence = dna_to_binary(dna_sequence)

# Split the binary sequence into odd and even indexed sequences
odd_indexed_sequence = binary_sequence[1::2]
even_indexed_sequence = binary_sequence[::2]

dna_sequence, binary_sequence, odd_indexed_sequence, even_indexed_sequence

