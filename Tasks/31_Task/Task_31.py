def dfs(node, visited, graph):
    visited.add(node)
    component = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            component.extend(dfs(neighbor, visited, graph))
    return component

file_1 = open("15.txt", "r")
n, m = map(int, file_1.readline().rstrip('\n').split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, file_1.readline().rstrip('\n').split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
component = dfs(1, visited, graph)

print(len(component))
print(*sorted(component))
