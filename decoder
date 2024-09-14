class SCLDecoder:
    def __init__(self, n, L, crc_poly):
        self.n = n  # Code length (2^n)
        self.L = L  # List size
        self.crc_poly = crc_poly  # CRC polynomial
    
    def polar_transform_matrix(self, n):
        # Kronecker product to generate the polar transformation matrix
        F = np.array([[1, 0], [1, 1]])
        G_n = F
        for _ in range(n - 1):
            G_n = np.kron(G_n, F)
        return G_n

    def decode(self, received_bits, drift_vector):
        # Initialize list decoding paths
        paths = [(np.zeros(2 ** self.n), 0)]  # (decoded sequence, path metric)
        
        for i in range(2 ** self.n):
            new_paths = []
            for path, metric in paths:
                # For each path, consider 0 and 1 as the next bit
                for bit in [0, 1]:
                    new_path = np.copy(path)
                    new_path[i] = bit
                    
                    # Adjust for drift (insertions/deletions)
                    if drift_vector[i] == 1:
                        # Modify the path based on drift
                        new_path[i] = 1 - bit
                    
                    new_metric = metric + self.path_metric(received_bits, new_path)
                    new_paths.append((new_path, new_metric))
            
            # Sort paths by metric and prune to list size L
            paths = sorted(new_paths, key=lambda x: x[1])[:self.L]
        
        # Perform CRC check on each path and select the best one
        best_path = self.crc_check(paths)
        return best_path
    
    def path_metric(self, received_bits, path):
        # Calculate the path metric (Hamming distance or other metric)
        return np.sum(received_bits != path)
    
    def crc_check(self, paths):
        for path, metric in paths:
            crc_value = crc_checksum(path)
            if crc_value == 0:  # Valid path with correct CRC
                return path
        # If no valid CRC, return the path with the best metric
        return paths[0][0]
