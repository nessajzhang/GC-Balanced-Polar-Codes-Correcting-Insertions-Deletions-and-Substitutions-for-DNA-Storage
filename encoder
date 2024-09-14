import numpy as np

def polar_transform_matrix(n):
    """Generate polar transform matrix using Kronecker product."""
    F = np.array([[1, 0], [1, 1]])
    G_n = F
    for _ in range(n - 1):
        G_n = np.kron(G_n, F)
    return G_n

def polar_encode(message, G):
    """Encode message using polar codes."""
    return np.dot(message, G) % 2

def find_balanced_vector(c_prime, B):
    """Find a balanced vector b for codeword c_prime."""
    length = len(c_prime)
    min_imbalance = float('inf')
    best_vector = np.zeros(length, dtype=int)
    
    # Use a more efficient method for large B
    if len(B) > 20:  # Threshold can be adjusted
        return find_balanced_vector_greedy(c_prime, B)
    
    for candidate in range(2**len(B)):
        b = np.zeros(length, dtype=int)
        b[B] = list(map(int, bin(candidate)[2:].zfill(len(B))))
        
        c_prime_plus_b = (c_prime + b) % 2
        imbalance = np.abs(np.sum(c_prime_plus_b) - length / 2)
        
        if imbalance < min_imbalance:
            min_imbalance = imbalance
            best_vector = b
    
    return best_vector

def find_balanced_vector_greedy(c_prime, B):
    """Find a balanced vector b using a greedy approach."""
    length = len(c_prime)
    b = np.zeros(length, dtype=int)
    current_sum = np.sum(c_prime)
    
    for index in B:
        if current_sum < length / 2:
            b[index] = 1
            current_sum += 1
        else:
            break
    
    return b

def polar_code_encoding(message, k, B, construction='standard'):
    """
    Encode a message using polar codes with reduced codeword imbalance.
    
    Args:
    message (np.array): The message to encode.
    k (int): Number of information bits.
    B (list): Indexes where zeros are to be inserted.
    construction (str): Type of polar code construction ('standard' or 'custom').
    
    Returns:
    np.array: The encoded codeword.
    """
    n = int(np.ceil(np.log2(k)))
    N = 2**n
    
    if len(message) != k:
        raise ValueError("Message length must be equal to k.")
    
    if max(B) >= N:
        raise ValueError("All indices in B must be less than N.")
    
    G = polar_transform_matrix(n)
    
    k_prime = k - len(B)
    m_prime = np.zeros(N, dtype=int)
    
    non_B_indices = np.setdiff1d(range(N), B)
    if len(non_B_indices) < k_prime:
        raise ValueError("Not enough non-B indices available to place all message bits.")
    
    m_prime[non_B_indices[:k_prime]] = message
    
    c_prime = polar_encode(m_prime, G)
    
    b = find_balanced_vector(c_prime, B)
    
    c = (c_prime + b) % 2
    return c

# Example usage
k = 128
B = [5, 10, 15, 20, 25, 30, 35, 40]
message = np.random.randint(2, size=k)

encoded_codeword = polar_code_encoding(message, k, B)
print("Encoded codeword:", encoded_codeword)
print("Codeword imbalance:", abs(np.sum(encoded_codeword) - len(encoded_codeword)/2))
