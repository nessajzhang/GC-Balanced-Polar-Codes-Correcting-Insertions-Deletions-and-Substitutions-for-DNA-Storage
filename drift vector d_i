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

# Example parameters
D = 3  # Example value for D
p_i = 0.4  # Example value for p_i
p_d = 0.3  # Example value for p_d

# Build the transition matrix
transition_matrix = build_transition_matrix(D, p_i, p_d)

print("Transition Matrix:\n", transition_matrix)
