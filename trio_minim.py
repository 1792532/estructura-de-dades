
def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    grau = [0] * (n + 1)

    for u, v in edges:
        adj[u][v] = True
        adj[v][u] = True
        grau[u] += 1
        grau[v] += 1

    minim = float('inf')

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if not adj[i][j]:
                continue

            for k in range(j + 1, n + 1):
                if adj[i][k] and adj[j][k]:
                    grau_trio = grau[i] + grau[j] + grau[k] - 6
                    minim = min(minim, grau_trio)

    if minim == float('inf'):
        return -1

    return minim
