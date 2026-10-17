
LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:

    def __init__(self, cap=13):
        self._table = [[None, None, LLIURE] for _ in range(cap)]
        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)

    def _find(self, key):
        m = len(self._table)
        j = self._hash_function(key)

        for i in range(m):
            pos = (j + i) % m

            if self._table[pos][2] == LLIURE:
                return None

            if self._table[pos][2] == OCUPAT and self._table[pos][0] == key:
                return pos

        return None

    def put(self, key: int, value: int) -> None:
        m = len(self._table)
        j = self._hash_function(key)
        first_deleted = None

        for i in range(m):
            pos = (j + i) % m
            entry = self._table[pos]

            if entry[2] == OCUPAT:
                if entry[0] == key:
                    entry[1] = value
                    return

            elif entry[2] == ESBORRAT:
                if first_deleted is None:
                    first_deleted = pos

            else:
                if first_deleted is not None:
                    pos = first_deleted

                self._table[pos] = [key, value, OCUPAT]
                self._n += 1

                if self._n > len(self._table) // 2:
                    self._resize(2 * len(self._table) - 1)

                return

        if first_deleted is not None:
            self._table[first_deleted] = [key, value, OCUPAT]
            self._n += 1

            if self._n > len(self._table) // 2:
                self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        pos = self._find(key)

        if pos is not None:
            return self._table[pos][1]

        return -1

    def remove(self, key: int) -> None:
        pos = self._find(key)

        if pos is not None:
            self._table[pos] = [None, None, ESBORRAT]
            self._n -= 1

    def _resize(self, c):
        old_table = self._table

        self._table = [[None, None, LLIURE] for _ in range(c)]
        self._n = 0

        for entry in old_table:
            if entry[2] == OCUPAT:
                self.put(entry[0], entry[1])

    def __len__(self):
        return self._n
