
class MyHashMap:
    

    def __init__(self, cap=13):
        self._table = cap * [None]
        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)

    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        self._bucket_put(j, key, value)

        # Redimensionem si el factor de carrega supera 0.5
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def _bucket_put(self, j, key, value):
        # Si el bucket esta buit, creem una llista
        if self._table[j] is None:
            self._table[j] = []

        # Busquem si la clau ja existeix al bucket
        for parella in self._table[j]:
            if parella[0] == key:
                parella[1] = value
                return

        # Si no existeix, afegim una parella nova
        self._table[j].append([key, value])
        self._n += 1

    def get(self, key: int) -> int:
        j = self._hash_function(key)
        return self._bucket_get(j, key)

    def _bucket_get(self, j, key):
        # Si no hi ha cap bucket, la clau no existeix
        if self._table[j] is None:
            return -1

        # Busquem la clau dins del bucket
        for parella in self._table[j]:
            if parella[0] == key:
                return parella[1]

        return -1

    def remove(self, key: int) -> None:
        j = self._hash_function(key)
        self._bucket_remove(j, key)

    def _bucket_remove(self, j, key):
        # Si el bucket esta buit, no hem de fer res
        if self._table[j] is None:
            return

        # Busquem i eliminem la parella corresponent
        for i in range(len(self._table[j])):
            if self._table[j][i][0] == key:
                self._table[j].pop(i)
                self._n -= 1

                # Si el bucket queda buit, el tornem a None
                if len(self._table[j]) == 0:
                    self._table[j] = None

                return

    def _resize(self, c):
        # Guardem la taula antiga
        old_table = self._table

        # Creem una taula nova de mida c
        self._table = c * [None]

        # Reiniciem el comptador per tornar a inserir les claus
        self._n = 0

        # Recalculem la posicio de cada clau amb la mida nova
        for bucket in old_table:
            if bucket is not None:
                for parella in bucket:
                    key = parella[0]
                    value = parella[1]
                    j = self._hash_function(key)
                    self._bucket_put(j, key, value)

    def __len__(self):
        return self._n
