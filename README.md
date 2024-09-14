# GC-Balanced Polar Codes Correcting Insertions, Deletions, and Substitutions for DNA Storage
This repository contains the implementation of the GC-balanced polar codes proposed in the article "GC-Balanced Polar Codes Correcting Insertions, Deletions, and Substitutions for DNA Storage" for correcting insertion, deletion, and substitution errors in DNA storage systems.
## Overview
DNA storage offers a promising solution for long-term data storage due to its high density and stability. However, DNA synthesis and sequencing processes introduce various errors, including insertions, deletions, and substitutions. This project aims to address these errors using GC-balanced polar codes, which are specifically designed for DNA storage channels.
## Features
* **GC-Balanced Polar Codes**: The proposed codes ensure a balanced GC content in the encoded DNA sequences, which is crucial for maintaining the stability and reliability of DNA molecules during laboratory operations.
* **Error Correction**: The codes effectively correct insertion, deletion, and substitution errors, improving the accuracy of DNA storage systems.
* **Efficient Algorithms**: The encoding and decoding algorithms have a computational complexity of O(N log N) with respect to the code length N, making them suitable for practical applications.
## Files
* **SCLDecoder.py**: Implements the Successive Cancellation List (SCL) decoding algorithm with modifications for IDS channels.
* **calculate_probability.py**: Calculates the probability of the i-th information bit given the received word and the current decoding information.
* **crc.py**: Implements the CRC (Cyclic Redundancy Check) for error detection.
* **dna_error_simulation.py**: Simulates the DNA storage channel with insertion, deletion, and substitution errors.
* **dna_sequence_generator_and_binary_converter.py**: Generates random DNA sequences and converts them to binary representation.
* **drift_vector.py**: Represents the drift vector and provides functions for manipulating it.
* **encoder.py**: Implements the GC-balanced polar encoding algorithm.
* **example_for_decoding.py**: Provides an example of how to use the SCL decoder.
* **ids_symmetric_capacity_estimator.py**: Estimates the symmetric capacity of IDS channels.
## Usage
To use this project, you need to install the required dependencies, including NumPy. You can then run the provided scripts to perform encoding, decoding, and simulation experiments.
## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you would like to contribute to this project.
## License
This project is licensed under the MIT License.
