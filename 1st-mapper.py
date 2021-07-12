import sys
def map_func(sents):
    data=sents.strip().split('\t')
    sent=data[2]
    for token in sent.strip().split():
for tokens in sys.stdin:
    for key,value in map_func(tokens):  
        print(key+"|"+str(value))