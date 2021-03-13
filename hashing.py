
STARTING_SIZE = 8923

class HashTable():

    def __init__(self):
        self._size = STARTING_SIZE
        self._slots = [None for i in range(0, self._size)]

    def get(self, key):
        idx = hash(key) % self._size
        l = self._slots[idx]

        if l:
            for (k,v) in l:
                if k == key:
                    return v

        return None

    def put(self, key, value):
        idx = hash(key) % self._size
        l = self._slots[idx]

        if not l:
            l = []

        found = False
        i = 0

        for (k,v) in l:
            if k == key:
                found = True
                continue
            i += 1
                

        if found:
            l[i] = (key, value)
        else:
            l.append((key, value))
        
        self._slots[idx] = l



