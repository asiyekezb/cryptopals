#!/usr/bin/env python
# Fixed XOR

import sys

def hex_to_bits(hex):
    bits = []
    for char in hex:
        num = int(char, base=16)
        bits.append(1 if num & 0b1000 else 0)
        bits.append(1 if num & 0b0100 else 0)
        bits.append(1 if num & 0b0010 else 0)
        bits.append(1 if num & 0b0001 else 0)
    return bits


HEX_DIGITS = [
    *(str(d) for d in range(0, 10)),
    'A',
    'B',
    'C',
    'D',
    'E',
    'F'
]
assert len(HEX_DIGITS) == 16

def bits_to_hex(bits):
    out = []
    for i in range(0, len(bits), 4):
        b0, b1, b2, b3 = bits[i:i+4]
        n = (((b0*2 + b1) * 2) + b2) * 2 + b3
        out.append(HEX_DIGITS[n])
    return ''.join(out)


def xor(bits1, bits2):
    return [
        1 if b1 != b2 else 0 for b1, b2 in zip(bits1, bits2)
    ]


if __name__ == '__main__':
    hex1, hex2 = sys.argv[1:]
    bits1 = hex_to_bits(hex1)
    # print(bits1)
    bits2 = hex_to_bits(hex2)
    # print(bits2)
    # print(bits_to_hex(bits1))
    # print(bits_to_hex(bits2))
    bits_out = xor(bits1, bits2)
    print(bits_to_hex(bits_out))
