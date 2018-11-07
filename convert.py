#!/usr/bin/env python

import sys
import os
import bech32

__VERSION__="0.1"

# define map of prefixes we can convert, as these are known.
prefix_map = {
  'cosmosaccaddr': 'cosmos',
  'cosmosaccpub':  'cosmospub',
  'cosmosvaladdr': 'cosmosvaloper',
  'cosmosvalpub':  'cosmosvaloperpub'
}


def main(key):
    ''' Main application logic
    '''
    welcome()
    # Basic error checking
    if key is None:
        usage()
  
    if not any([key.startswith(x) for x in prefix_map]):
        invalid(key)

    # Decode existing key
    hrp,decoded_pubkey=bech32decode(key)
    
    # Error if parsing legacy key failed
    if decoded_pubkey is False:
        invalid(key)

    # Determine prefix from map
    new_prefix = prefix_map.get(hrp)

    # Convert, and display result
    print ("Old Key: {}\nNew Key: {}\n".format(key, bech32encode(new_prefix, decoded_pubkey)))
    

def welcome():
    ''' Print a nice little welcome message
    '''
    print("\nBech32 convertor v{}\nBy Chorus One Inc. [ joe@chorus.one | https://chorus.one ]\n".format(__VERSION__))


def invalid(key):
    ''' Display warning for invalid format key
    '''
    print("ERROR: {} is an invalid legacy cosmos-sdk bech32 key\n".format(key))
    usage()


def usage():
    ''' Print usage instructions
    '''
    print("Usage:\n\nconvert.py <legacy cosmos bech32 key>\n")
    sys.exit(255)


def bech32encode(hrp, data):
    ''' Encode a bech32 string given prefix and bytearray
    '''
    converted = bech32.convertbits(data, 8, 5, True)
    return bech32.bech32_encode(hrp, converted)


def bech32decode(bech):
    ''' Decode bech32 string into prefix and bytearray of data
    '''
    hrp, data = bech32.bech32_decode(bech)
    # Return early if we couldn't parse the input string
    if data is None:
        return hrp,False
    converted = bech32.convertbits(data, 5, 8, False)
    return hrp,converted


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) == 2 else None)
