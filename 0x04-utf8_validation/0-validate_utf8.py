#!/usr/bin/python3
""" The UTF-8 Validation """


def get_leading_set_bits(num):
    """ Returning number of leading set bits 1 """
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """ Determining if given data set is representing valid UTF-8 encoding """
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])
            ''' 1-byte -format: 0xxxxxxx-'''
            if bits_count == 0:
                continue
            ''' Character in the UTF-8 can be 1 to 4 bytes long'''
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            ''' Checking if current byte has the format 10xxxxxx '''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
