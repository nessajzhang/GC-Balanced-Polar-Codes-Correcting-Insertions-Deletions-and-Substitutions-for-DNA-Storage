import numpy as np  # Import numpy for array handling
from drift_vector import markov_drift_vector  # Import the function
from SCLDecoder import SCLDecoder  # Import the SCL decoder

# Parameters for Polar code
N = 16  # Code length (2^n)
K = 8   # Number of information bits
L = 8   # List size for SCL decoding

# Example received sequence (simulated with noise)
received_sequence = np.array([0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0])

# Parameters for drift vector generation
D = len(received_sequence)
p_i = 0.01  # Probability of insertion
p_d = 0.01  # Probability of deletion

# Generate drift vector using Markov process
drift_vector = markov_drift_vector(D, p_i, p_d)

# Initialize the SCL decoder
scl_decoder = SCLDecoder(N=N, K=K, L=L)

# Perform decoding with drift vector taken into account
decoded_sequence = scl_decoder.decode(received_sequence)

print("Decoded sequence:", decoded_sequence)
