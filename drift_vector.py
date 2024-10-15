import numpy as np

def build_transition_matrix(D, p_i, p_d):
    size = 2 * D + 1
    P = np.zeros((size, size))
    
    # Define the state index mapping
    def state_index(d):
        return d + D
    
    for d in range(-D, D + 1):
        i = state_index(d)
        if d > -D:
            P[i, state_index(d - 1)] = p_d
        if d < D:
            P[i, state_index(d + 1)] = p_i
        if d > -D and d < D:
            P[i, state_index(d)] = 1 - p_i - p_d
        elif d == -D:
            P[i, state_index(d)] = 1 - p_i
        elif d == D:
            P[i, state_index(d)] = 1 - p_d
    
    return P

def markov_drift_vector(D, p_i, p_d):
    """
    Generate a drift vector using a Markov process.
    
    Args:
    D (int): Length of the drift vector
    p_i (float): Probability of insertion
    p_d (float): Probability of deletion
    
    Returns:
    numpy.array: Drift vector
    """
    drift_vector = np.zeros(D, dtype=int)
    current_state = 0
    
    for i in range(D):
        if current_state == 0:
            # No drift
            if np.random.random() < p_i:
                current_state = 1  # Insertion
            elif np.random.random() < p_d:
                current_state = -1  # Deletion
        elif current_state == 1:
            # After insertion
            if np.random.random() < p_d:
                current_state = 0  # Back to no drift
        elif current_state == -1:
            # After deletion
            if np.random.random() < p_i:
                current_state = 0  # Back to no drift
        
        drift_vector[i] = current_state
    
    return drift_vector

# Example parameters
D = 3  # Example value for D
p_i = 0.4  # Example value for p_i
p_d = 0.3  # Example value for p_d

# Build the transition matrix
transition_matrix = build_transition_matrix(D, p_i, p_d)

print("Transition Matrix:\n", transition_matrix)
