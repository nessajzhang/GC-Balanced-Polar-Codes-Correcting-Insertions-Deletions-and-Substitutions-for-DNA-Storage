import numpy as np
from typing import List, Tuple, Dict

class SCLDecoder:
    def __init__(self, N: int, K: int, L: int, pi: float, pd: float, ps: float):
        """
        Initialize the SCL decoder.
        
        Args:
        N (int): Code length (must be a power of 2)
        K (int): Number of information bits
        L (int): List size
        pi (float): Insertion probability
        pd (float): Deletion probability
        ps (float): Substitution probability
        """
        self.N = N
        self.K = K
        self.L = L
        self.n = int(np.log2(N))
        self.pi = pi
        self.pd = pd
        self.ps = ps
        
        # Initialize paths
        self.paths = [{'bits': np.zeros(N, dtype=int), 'prob': 1.0, 'drift': np.zeros(N, dtype=int)} for _ in range(L)]
        
        # Initialize LLR storage
        self.llr = np.zeros((self.n + 1, N, L))
        
        # Generate frozen bit positions (simplified)
        self.frozen_bits = set(range(K, N))
        
        # Current bit being decoded
        self.current_bit = 0

    def f_function(self, a: float, b: float) -> float:
        """f function for LLR calculation."""
        return np.sign(a) * np.sign(b) * np.minimum(np.abs(a), np.abs(b))

    def g_function(self, a: float, b: float, u: int) -> float:
        """g function for LLR calculation."""
        return b + (1 - 2 * u) * a

    def channel_llr(self, y: np.ndarray, d: int, i: int) -> float:
        """
        Calculate channel LLR for IDS channel.
        
        Args:
        y (np.ndarray): Received sequence
        d (int): Current drift value
        i (int): Bit index
        
        Returns:
        float: Channel LLR
        """
        if i + d >= len(y) or i + d < 0:
            # If the bit is outside the received sequence due to drift,
            # we return a neutral LLR (equal probability for 0 and 1)
            return 0
        
        # Calculate LLR based on the channel model
        p_y_given_x_0 = (1 - self.ps) if y[i + d] == 0 else self.ps
        p_y_given_x_1 = (1 - self.ps) if y[i + d] == 1 else self.ps
        
        return np.log(p_y_given_x_0 / p_y_given_x_1)

    def calculate_llr(self, y: np.ndarray, d: int, level: int, i: int, path_index: int) -> float:
        """
        Recursively calculate LLR.
        
        Args:
        y (np.ndarray): Received sequence
        d (int): Current drift value
        level (int): Current level in the decoding tree
        i (int): Bit index
        path_index (int): Index of the current path
        
        Returns:
        float: Calculated LLR
        """
        if level == self.n:
            return self.channel_llr(y, d, i)
        
        length = self.N // (2 ** level)
        left_llr = self.calculate_llr(y, d, level + 1, 2 * i, path_index)
        right_llr = self.calculate_llr(y, d, level + 1, 2 * i + 1, path_index)
        
        if i % 2 == 0:
            return self.f_function(left_llr, right_llr)
        else:
            u_partial = self.paths[path_index]['bits'][i - 1]
            return self.g_function(left_llr, right_llr, u_partial)

    def select_paths(self) -> List[Tuple[Dict, int, float]]:
        """Select the most probable paths."""
        all_paths = []
        for path_index, path in enumerate(self.paths):
            llr = self.llr[0, self.current_bit, path_index]
            prob_0 = path['prob'] * (1 / (1 + np.exp(-llr)))
            prob_1 = path['prob'] * (1 / (1 + np.exp(llr)))
            all_paths.append((path, 0, prob_0))
            all_paths.append((path, 1, prob_1))
        
        all_paths.sort(key=lambda x: x[2], reverse=True)
        return all_paths[:self.L]

    def extend_paths(self, selected_paths: List[Tuple[Dict, int, float]]):
        """Extend the selected paths."""
        new_paths = []
        for old_path, bit, prob in selected_paths:
            new_path = {
                'bits': old_path['bits'].copy(),
                'prob': prob,
                'drift': old_path['drift'].copy()
            }
            new_path['bits'][self.current_bit] = bit
            
            # Update drift based on the decoded bit
            r = np.random.random()
            if r < self.pi:
                new_path['drift'][self.current_bit] = new_path['drift'][self.current_bit - 1] + 1
            elif r < self.pi + self.pd:
                new_path['drift'][self.current_bit] = new_path['drift'][self.current_bit - 1] - 1
            else:
                new_path['drift'][self.current_bit] = new_path['drift'][self.current_bit - 1]
            
            new_paths.append(new_path)
        self.paths = new_paths

    def decode(self, y: np.ndarray) -> np.ndarray:
        """
        Main decoding function.
        
        Args:
        y (np.ndarray): Received sequence
        
        Returns:
        np.ndarray: Decoded message
        """
        for i in range(self.N):
            self.current_bit = i
            
            for path_index, path in enumerate(self.paths):
                current_drift = path['drift'][i - 1] if i > 0 else 0
                self.llr[0, i, path_index] = self.calculate_llr(y, current_drift, 0, i, path_index)
            
            if i not in self.frozen_bits:
                selected_paths = self.select_paths()
                self.extend_paths(selected_paths)
            else:
                for path in self.paths:
                    path['bits'][i] = 0
                    # Update drift for frozen bits too
                    if i > 0:
                        path['drift'][i] = path['drift'][i - 1]
        
        best_path = max(self.paths, key=lambda x: x['prob'])
        return best_path['bits'][:self.K]
