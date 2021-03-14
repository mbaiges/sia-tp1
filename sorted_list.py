class ListElement:
    def __init__(self, data, next_el = None):
        self.data = data
        self.next_el = next_el

    def set_next(self, next_el):
        self.next_el = next_el

    def get_next(self):
        return self.next_el

    def get_data(self):
        return self.data

class OrderedList:
    def __init__(self, cmp):
        self.head = None
        self.size = 0
        self.cmp = cmp
        
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if cmp(current.get_data(), item) > 0:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if self.cmp(current.get_data(), item) > 0:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = ListElement(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        self.size += 1

    def pop(self):
        ret = self.head
        self.head = self.head.get_next()
        self.size -= 1
        return ret.get_data()
        
    def length(self):
        return self.size