import numpy as np
from typing import Tuple

class IDSChannel:
    def __init__(self, pi: float, pd: float, ps: float):
        self.pi = pi
        self.pd = pd
        self.ps = ps

    def transmit(self, x: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        y = []
        d = np.zeros(len(x), dtype=int)
        current_drift = 0

        for i, bit in enumerate(x):
            r = np.random.random()
            if r < self.pi:  # Insertion
                y.append(np.random.randint(2))
                current_drift += 1
            elif r < self.pi + self.pd:  # Deletion
                current_drift -= 1
                continue
            
            # Transmission (with possible substitution)
            if np.random.random() < self.ps:
                y.append(1 - bit)
            else:
                y.append(bit)
            
            d[i] = current_drift

        return np.array(y), d

def estimate_symmetric_capacity(pi: float, pd: float, ps: float, N: int, M: int) -> float:
    """
    Estimate the symmetric capacity of the IDS channel using Monte Carlo simulation.
    
    Args:
    pi (float): Insertion probability
    pd (float): Deletion probability
    ps (float): Substitution probability
    N (int): Length of input sequence
    M (int): Number of Monte Carlo trials
    
    Returns:
    float: Estimated symmetric capacity
    """
    channel = IDSChannel(pi, pd, ps)
    
    total_mutual_info = 0
    
    for _ in range(M):
        # Generate random input sequence
        x = np.random.randint(2, size=N)
        
        # Transmit through the channel
        y, d = channel.transmit(x)
        
        # Calculate mutual information for this trial
        mutual_info = calculate_mutual_information(x, y, d, pi, pd, ps)
        
        total_mutual_info += mutual_info
    
    # Average mutual information over all trials
    avg_mutual_info = total_mutual_info / M
    
    # Symmetric capacity estimation
    symmetric_capacity = avg_mutual_info / N
    
    return symmetric_capacity

def calculate_mutual_information(x: np.ndarray, y: np.ndarray, d: np.ndarray, pi: float, pd: float, ps: float) -> float:
    """
    Calculate the mutual information for a single transmission.
    
    Args:
    x (np.ndarray): Input sequence
    y (np.ndarray): Output sequence
    d (np.ndarray): Drift sequence
    pi (float): Insertion probability
    pd (float): Deletion probability
    ps (float): Substitution probability
    
    Returns:
    float: Calculated mutual information
    """
    N = len(x)
    L = len(y)
    
    # Calculate P(Y|X)
    log_p_y_given_x = 0
    j = 0
    for i in range(N):
        if j >= L:  # All remaining bits were deleted
            log_p_y_given_x += np.log(pd)
        elif d[i] > d[i-1] if i > 0 else d[i] > 0:  # Insertion occurred
            log_p_y_given_x += np.log(pi / 2)
            j += 1
        elif j == L or (i < N-1 and d[i+1] < d[i]):  # Deletion occurred
            log_p_y_given_x += np.log(pd)
        else:  # Normal transmission or substitution
            p_bit = ps if y[j] != x[i] else (1 - ps)
            log_p_y_given_x += np.log((1 - pi - pd) * p_bit)
            j += 1
    
    # Calculate P(Y)
    log_p_y = L * np.log(0.5)  # Assuming equally likely bits
    
    # Mutual information
    mutual_info = log_p_y_given_x - log_p_y
    
    return mutual_info

# Example usage
pi, pd, ps = 0.1, 0.1, 0.1
N = 1000
M = 10000

estimated_capacity = estimate_symmetric_capacity(pi, pd, ps, N, M)
print(f"Estimated symmetric capacity: {estimated_capacity}")
