from tqdm import tqdm
import itertools
from itertools import combinations
from multiprocessing import Pool
import sys
import time
import threading

def products(x):
    for i in x[-1]:
        yield x[:-1]+[i]
        
def insert(nums):
    s1,s2=nums[0],nums[1]
    n1,n2=convert(s1),convert(s2)
    return [f"{s1}+{s2}", f"{s1}-{s2}", f"{s2}-{s1}", f"{n1}*{n2}", f"{n1}/{n2}", f"{n2}/{n1}"]



def convert(i):
    return f"({i})" if ("+" in i or "-" in i) else i

def execute(i,targetn):
    try:
        if eval(i)==targetn:
            return i
        else:
            return False
    except ZeroDivisionError:
        return False

def get1(x):
    if len(x)>2:
        for comb in combinations(x,2):
            y=sorted(x,key=(list(comb)+x).index)[2:]
            y.append(insert(comb))
            for i in products(y):
                yield from get1(i)
    else:
        for i in insert(x):
            yield i

done=False
    
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rGenerating all expressions  ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')
    
def task():
    global done
    p2=Pool(16)
    s=time.time()
    print("input numbers with space like '1 2 3 4'")
    x=input().split(" ")
    targetn=int(input("input target number. > "))
    t = threading.Thread(target=animate)
    t.start()
    y=set(get1(x))
    z=list(map(lambda i:(i,targetn),y))
    done=True
    print(list(filter(lambda i:i,p2.starmap(execute,tqdm(z)))))
    e=time.time()
    print(f"Took {e-s}s")

if __name__=="__main__":
    task()
