import math
import time

STARTING_SIZE = 1361
COLLISIONS_THRESHOLD = 0.3

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

class HashTable():

    def __init__(self):
        self._size = STARTING_SIZE
        self._slots = [None for i in range(0, self._size)]
        self._used_slots = 0
        self._collisions = 0

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
            self._used_slots += 1

            if len(l) > 1:
                self._collisions += 1

        self._check_resize()
        
        self._slots[idx] = l

    def _check_resize(self):
        if (1.0 * self._collisions) / self._used_slots > COLLISIONS_THRESHOLD:
            self._resize()

    def _resize(self):
        n = self._size * 2 + 1 # odd

        prime_found = False

        while not prime_found:
            if is_prime(n):
                prime_found = True
            else:
                n += 2 # we know is odd n

        self._size = n

        self._collisions = 0
        self._used_slots = 0

        old_slots = self._slots

        self._slots = [None for i in range(0, self._size)]

        for l in old_slots:
            if l != None:
                for (k,v) in l:
                    self.put(k, v) 
