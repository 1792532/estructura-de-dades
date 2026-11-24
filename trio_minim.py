def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    # Creem una matriu per consultar si dos nodes estan connectats
    adj = [[False] * (n + 1) for _ in range(n + 1)]

    # Guardem el grau de cada node
    grau = [0] * (n + 1)

    # Afegim les arestes i actualitzem els graus
    for u, v in edges:
        adj[u][v] = True
        adj[v][u] = True
        grau[u] += 1
        grau[v] += 1

    # Inicialitzem el grau minim
    minim = float('inf')

    # Busquem tots els possibles trios
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):

            # Si no estan connectats, no poden formar un trio
            if not adj[i][j]:
                continue

            for k in range(j + 1, n + 1):

                # Comprovem si els tres nodes estan connectats
                if adj[i][k] and adj[j][k]:

                    # Restem les 6 connexions internes del trio
                    grau_trio = grau[i] + grau[j] + grau[k] - 6

                    # Actualitzem el grau minim
                    minim = min(minim, grau_trio)

    # Si no hi ha cap trio, retornem -1
    if minim == float('inf'):
        return -1

    return minim


if __name__ == "__main__":
    # Exemple 1: resultat esperat 3
    print(minTrioDegree(6, [
        [1, 2], [1, 3], [2, 3],
        [1, 4], [2, 5], [3, 6],
        [4, 5], [5, 6]
    ]))

    # Exemple 2: resultat esperat 1
    print(minTrioDegree(7, [
        [1, 2], [2, 3], [3, 1],
        [3, 4], [4, 5], [5, 6],
        [6, 4], [6, 7]
    ]))

