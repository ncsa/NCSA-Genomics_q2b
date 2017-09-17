""" q2b.py - Ryan Chui (2017) """

import sys
import Modules.Encode as Encode

def main():
    """ Either encode or decode a fastq file.

    Expects:
        python3+ q2b.py [-e/-d] [/input/path] [/output/path]
    """

    with open(sys.argv[2], 'r') as i_stream:
        with open(sys.argv[3], 'a') as o_stream:
            line_number = 0
            for line in i_stream:
                # print(line_number, line)
                if line_number == 2:
                    Encode.encode(line.strip(), o_stream)
                else:
                    if line[0] == '@':
                        line_number = 1
                    o_stream.write(line)
                line_number += 1
if __name__ == "__main__":
    main()
