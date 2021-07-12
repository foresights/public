import sys
def reduce_func(token,results):
    return token,sum(results)                        
last_k=None
results=[]
for tokens in sys.stdin:
    k,v=tokens.strip().split('|')  
    if k!=last_k and last_k is not None:
        k_result,v_result=reduce_func(last_k,results)
        print(k_result+"|"+str(v_result))
        results=[]
    last_k=k
    results.append(int(v))
if last_k is not None:
    k_result,v_result=reduce_func(prev_key,results)
    print(k_result+"|"+str(v_result))     