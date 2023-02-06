computers = int(input())
pair = int(input())

graph = [[] * computers for _ in range(computers + 1)]
visited = [0] * (computers+1)
cnt = 0

for i in range(pair):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
            
dfs(1)
print(cnt)