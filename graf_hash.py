
class GrafHash:

    def __init__(self, ln=None, lv=None, lp=None):

        # Diccionari on guardem els vertexs i els seus veins
        self._graf = {}

        # Comptadors del nombre de vertexs i arestes
        self._num_vertices = 0
        self._num_edges = 0

        # Afegim els vertexs inicials
        if ln is not None:
            for x in ln:
                self.insert_vertex(x)

        # Afegim les arestes inicials
        if lv is not None:
            for i in range(len(lv)):

                n1 = lv[i][0]
                n2 = lv[i][1]

                # Si no hi ha pesos, posem pes 1
                if lp is None:
                    p = 1
                else:
                    p = lp[i]

                self.insert_edge(n1, n2, p)

    def insert_vertex(self, x) -> None:

        # Comprovem que el vertex no existeixi
        if x not in self._graf:

            # Afegim el vertex amb un diccionari buit
            self._graf[x] = {}

            # Actualitzem el nombre de vertexs
            self._num_vertices += 1

    def insert_edge(self, n1, n2, p=1) -> None:

        # Comprovem si l'aresta ja existeix
        if n2 not in self._graf[n1]:
            self._num_edges += 1

        # Afegim l'aresta en els dos sentits
        self._graf[n1][n2] = p
        self._graf[n2][n1] = p

    def remove_edge(self, n1, n2) -> None:

        # Comprovem si l'aresta existeix
        if n2 in self._graf[n1]:

            # Esborrem l'aresta dels dos sentits
            del self._graf[n1][n2]
            del self._graf[n2][n1]

            # Actualitzem el nombre d'arestes
            self._num_edges -= 1

    def remove_vertex(self, x) -> None:

        # Comprovem si el vertex existeix
        if x in self._graf:

            # Recorrem tots els veins del vertex
            for vei in self._graf[x]:

                # Esborrem el vertex de la llista de veins
                del self._graf[vei][x]

                # Actualitzem el nombre d'arestes
                self._num_edges -= 1

            # Esborrem el vertex del graf
            del self._graf[x]

            # Actualitzem el nombre de vertexs
            self._num_vertices -= 1

    def has_edge(self, n1, n2) -> bool:

        # Comprovem que existeixin els dos vertexs
        if n1 not in self._graf or n2 not in self._graf:
            return False

        # Mirem si n2 es un vei de n1
        return n2 in self._graf[n1]

    def weight(self, n1, n2):

        # Si existeix l'aresta, retornem el seu pes
        if self.has_edge(n1, n2):
            return self._graf[n1][n2]

        # Si no existeix, retornem None
        return None

    def degree(self, x) -> int:

        # Retornem el nombre de veins del vertex
        return len(self._graf[x])

    def num_vertices(self) -> int:

        # Retornem el nombre de vertexs
        return self._num_vertices

    def num_edges(self) -> int:

        # Retornem el nombre d'arestes
        return self._num_edges

    def vertices(self):

        # Retornem un iterador dels vertexs
        return iter(self._graf)

    def edges(self, x):

        # Retornem un iterador dels veins del vertex
        return iter(self._graf[x])


if __name__ == "__main__":

    g = GrafHash(
        ["Sants Est.", "Pl. Sants", "Hostafr."],
        [["Sants Est.", "Pl. Sants"], ["Pl. Sants", "Hostafr."]],
        [1585, 511]
    )

    print(g.has_edge("Pl. Sants", "Sants Est."))
    print(g.weight("Sants Est.", "Pl. Sants"))
    print(g.degree("Pl. Sants"))

    g.insert_vertex("Esp.")
    g.insert_edge("Hostafr.", "Esp.")

    print(g.weight("Esp.", "Hostafr."))
    print(g.num_edges())

    g.remove_vertex("Pl. Sants")

    print(g.has_edge("Sants Est.", "Pl. Sants"))
    print(g.num_edges())
    print(g.degree("Sants Est."))
    print(sorted(g.vertices()))
