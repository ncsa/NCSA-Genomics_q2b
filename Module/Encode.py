""" Encode.py - Ryan Chui (2017)

Encodes a fastq file to a fastb file.
"""

import sys

BASES_PER_BYTE = 3

def print_dict(input_dict):
    """ Prints a dictionary.

    Args:
        input_dict: Dictionary to be printed.

    Returns:
        None
    """
    for i, j in input_dict.items():
        print i, j

def encode():
    """ Prints a byte.

        A - 00
        C - 01
        G - 10
        T - 11

        byte = [base 2b] [base 2b] [base 2b] [delimiter 2b]
        delimiter = {
            00 - more
            01 - 1 missing
            11 - 2 missing
        }
    """

    base_dict = {}
    bases = ['A', 'C', 'G', 'T']
    byte_code = ['00', '01', '10', '11']

    for i in range(4):
        for j in range(4):
            for k in range(4):
                base_dict[bases[i] + bases[j] + bases[k]] \
                    = byte_code[i] + byte_code[j] + byte_code[k]

    byte_dict = {}
    for i, j in base_dict.items():
        byte_dict[j] = i

    # print_dict(base_dict)
    # print_dict(byte_dict)

    with open(sys.argv[1], 'r') as i_file:
        with open(sys.argv[2], 'w') as o_file:
            while True:
                seq_stream = i_file.read(BASES_PER_BYTE)
                if not seq_stream:
                    break
                else:
                    partial_length = len(seq_stream)
                    key = ''
                    value = ''
                    if partial_length == BASES_PER_BYTE:
                        for base in seq_stream:
                            key += base
                        value = base_dict[key] + '00'
                    else:
                        key = seq_stream
                        missing = BASES_PER_BYTE - partial_length
                        for base in seq_stream:
                            value += byte_code[bases.index(base)]
                        for i in range(missing):
                            value += '00'
                        if missing == 1:
                            value += '01'
                        else:
                            value += '11'
                    print key, value
                    o_file.write(chr(int(value[:8], base=2)))