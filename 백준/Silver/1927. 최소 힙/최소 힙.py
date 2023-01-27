import sys
import heapq

N = int(input())
heap = []

for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)