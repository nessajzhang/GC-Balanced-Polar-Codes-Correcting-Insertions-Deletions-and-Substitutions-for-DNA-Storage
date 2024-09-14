# Parameters for Polar code
n = 4  # Code length 2^n
L = 8  # List size for SCL decoding
crc_poly = 0b111001101  # CRC polynomial (x^8 + x^7 + x^6 + x^4 + x^2 + 1)

# Example received sequence (simulated with noise)
received_sequence = np.array([0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0])

# Generate drift vector using Markov process
drift_vector = markov_drift_vector(len(received_sequence), transition_matrix)

# Initialize the SCL decoder
scl_decoder = SCLDecoder(n=n, L=L, crc_poly=crc_poly)

# Perform decoding with drift vector taken into account
decoded_sequence = scl_decoder.decode(received_sequence, drift_vector)

print("Decoded sequence:", decoded_sequence)
