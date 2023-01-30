import random
import time
start = time.perf_counter()
def fib(n):
    if n == 0:
        return 0
    if n == 1 or n ==2:
        return 1
         
    else:
        return fib(n-1) + fib(n-2)
      
testNum = random.randint(15,35)
print("fib(" + str(testNum) + ")" + "=" + str(fib(testNum)))
end = time.perf_counter()
print(str(end-start) + " seconds")
