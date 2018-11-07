# cosmos-bech32-convertor
A Bech32 address convertor for Cosmos SDK

## Motivation

[Cosmos SDK](https://cosmos.network) implemented changes to the format of the bech32 address used on the Cosmos network between the 0.24.2 and 0.25 releases. This script enables users to convert between legacy (pre-0.25) cosmos-sdk bech32 addresses, and the 0.25+ format.


The script should be compatible with both python2 and python3.

This script was made possible using the bech32 python library, written by [Pieter Wuille](https://twitter.com/pwuille) which can be found [here](https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py)


## Usage

```
python convert.py <legacy bech32 address>
```


### Example

```
$ python3 convert.py cosmosaccpub1addwnpepqg5ec06deee7rk3s0xmwn0f3e66wv65l2xc07ynxzj67z9ld5dcwv6ljvv9

Bech32 convertor v0.1
By Chorus One Inc. [ joe@chorus.one | https://chorus.one ]

Old Key: cosmosaccpub1addwnpepqg5ec06deee7rk3s0xmwn0f3e66wv65l2xc07ynxzj67z9ld5dcwv6ljvv9
New Key: cosmospub1addwnpepqg5ec06deee7rk3s0xmwn0f3e66wv65l2xc07ynxzj67z9ld5dcwvwgyrcu
```

