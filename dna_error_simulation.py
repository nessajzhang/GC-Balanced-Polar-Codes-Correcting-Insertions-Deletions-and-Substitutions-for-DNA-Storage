import random

# Function to generate a random base (A, T, C, G)
def random_base():
    return random.choice(['A', 'T', 'C', 'G'])

# Function to introduce insertion, deletion, and substitution errors with given probabilities
def introduce_indel_errors(dna_sequence, insertion_prob=0.01, deletion_prob=0.01, substitution_prob=0.01):
    corrupted_sequence = []  # Initialize the list for the corrupted sequence
    
    i = 0
    while i < len(dna_sequence):
        rand_val = random.random()
        
        # Insertion error: insert a random base with the given probability
        if rand_val < insertion_prob:
            corrupted_sequence.append(random_base())  # Insert a random base
            continue  # Stay at the current position, no base deleted or replaced
        
        rand_val = random.random()
        
        # Deletion error: delete the current base with the given probability
        if rand_val < deletion_prob:
            i += 1  # Skip the current base, effectively deleting it
            continue
        
        rand_val = random.random()
        
        # Substitution error: replace the current base with a random base
        if rand_val < substitution_prob:
            corrupted_sequence.append(random_base())  # Substitute with a random base
        else:
            # No error, copy the original base
            corrupted_sequence.append(dna_sequence[i])
        
        i += 1  # Move to the next base
    
    return ''.join(corrupted_sequence)  # Convert list back to string

# Example DNA sequence
original_sequence = "ATCGTACGATCGTACG"

# Introduce errors with the specified probabilities
insertion_prob = 0.05  # Probability of insertion error
deletion_prob = 0.05   # Probability of deletion error
substitution_prob = 0.05  # Probability of substitution error

# Generate the corrupted sequence with errors
corrupted_sequence = introduce_indel_errors(original_sequence, insertion_prob, deletion_prob, substitution_prob)

print("Original sequence:", original_sequence)
print("Corrupted sequence:", corrupted_sequence)
