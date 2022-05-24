import time

start = time.time()

def subset(lim = 2, div = 5):
    lim+=1
    array = []
    subarr = []
    for i in range(lim):
        array.append(i)
    for i in range(len(array)+1):
        for j in range(i):
            subarr.append(array[j: i])
    sums = []
    def add(args):
        tot=0
        for i in range(len(args)):
            tot+=args[i]
        return tot
    sums = []
    for i in range(len(subarr)):
        sums.append(add(subarr[i]))
    count = 0
    for i in range(len(sums)):
        if sums[i]%div==0:
            count+=1
    return count


print(subset(2000, 5))
end = time.time()
print('Time elapsed: {} seconds'.format(round(end - start, 5), sep='\n'))
