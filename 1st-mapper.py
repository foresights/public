#! /usr/bin/env python3
import sys
def map_func(sents):
    data=sents.strip().split('\t')
    sent=data[0]
    for token in sent.strip().split():
        yield token,1
for tokens in sys.stdin:
    for k,v in map_func(tokens):
        print(k+"|"+str(v))