# CRC generation with g(x) = x^8 + x^7 + x^6 + x^4 + x^2 + 1
def crc_checksum(data_bits):
    # CRC polynomial g(x) = x^8 + x^7 + x^6 + x^4 + x^2 + 1
    generator = 0b111001101  # Binary representation of the polynomial
    data = data_bits << 8  # Shift to account for the 8-bit CRC
    
    for i in range(len(data_bits)):
        if data & (1 << (len(data_bits) + 7 - i)):  # Check leading bit
            data ^= generator << (len(data_bits) - i)  # XOR with generator
    
    return data & 0xFF  # Return the final 8-bit CRC

def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'."""
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]

def crc_check(input_bitstring, polynomial_bitstring, check_value):
    """Calculate the CRC check of a string of bits using a chosen polynomial."""
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ('1' not in ''.join(input_padded_array)[len_input:])
