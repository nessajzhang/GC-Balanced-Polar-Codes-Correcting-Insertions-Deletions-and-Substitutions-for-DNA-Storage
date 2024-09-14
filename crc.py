# CRC generation with g(x) = x^8 + x^7 + x^6 + x^4 + x^2 + 1
def crc_checksum(data_bits):
    # CRC polynomial g(x) = x^8 + x^7 + x^6 + x^4 + x^2 + 1
    generator = 0b111001101  # Binary representation of the polynomial
    data = data_bits << 8  # Shift to account for the 8-bit CRC
    
    for i in range(len(data_bits)):
        if data & (1 << (len(data_bits) + 7 - i)):  # Check leading bit
            data ^= generator << (len(data_bits) - i)  # XOR with generator
    
    return data & 0xFF  # Return the final 8-bit CRC
