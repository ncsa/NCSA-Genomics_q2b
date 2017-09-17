""" Encode.py - Ryan Chui (2017)

Encodes a fastq file to a fastb file.
"""

import os
import sys
import pprint
import multiprocessing

BYTE_CODE = {
    'A':'000', # A
    'C':'001', # C
    'G':'010', # G
    'T':'011', # T
    'N':'101', # Any
    'I':'111'  # Missing
}
BASES_PER_BYTE = 6

def print_dict(input_dict):
    """ Prints a dictionary.

    Args:
        input_dict: Dictionary to be printed.

    Returns:
        None
    """
    for i, j in input_dict.items():
        print(i, j)

def split_list(input_seq, split_size):
    """ Splits a list into chunks of a specific size.

    Args:
        input_list: The list to split.
        split_size: The size that each split should be.

    Returns:
        output_list: The list split into chunks
    """
    output_list = []
    for i in range(0, len(input_seq), split_size):
        output_list.append(input_seq[i:i + split_size])
    # pprint.pprint(output_list)
    return output_list

def convert_to_binary(sequence):
    key = ''
    value = ''
    sequence_length = len(sequence)
    if sequence_length == BASES_PER_BYTE:
        for base in sequence:
            key += base
            value += BYTE_CODE[base]
    else:
        missing_length = BASES_PER_BYTE - sequence_length
        # print(BASES_PER_BYTE, sequence_length, missing_length)
        for base in sequence:
            key += base
            value += BYTE_CODE[base]
        for i in range(missing_length):
            value += BYTE_CODE['I']
    return int(value, base=2)

def encode(input_seq, o_stream):
    """ Prints a byte.

        A - 000
        C - 001
        G - 010
        T - 011
        N - 100
        I - 101
    """

    # print_dict(byte_code)
    # print_dict(byte_dict)

    # print(input_seq)
    sequence_list = split_list(input_seq, BASES_PER_BYTE)

    pool = multiprocessing.Pool()

    for result in pool.imap(convert_to_binary, sequence_list):
        o_stream.write(chr(result))
    o_stream.write("\n")

    pool.close()
    pool.join()
