class Object:

    def __init__(self, id, name):
        self.id = id
        self.name = name
    

class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [None]*size

        print(self.table)



    def HashGenerator(self, index):

        return index%self.size
    

    def insert(self, object):
        
        index = self.HashGenerator(object.id)

        if self.table[index] is None:
            self.table[index] = [object]
        else:
            self.table[index].append(object)


    def delete(self, id):
        index = self.HashGenerator(id)

        if self.table[index] is not None:
            for object in self.table[index]:
                if object.id == id:
                    self.table[index].remove(object)
                    return
    

    def search(self, id):
        index = self.HashGenerator(id)

        if self.table[index] is not None:
            for object in self.table[index]:
                if object.id == id:
                    return object





table = HashTable(100)

object1 = Object(123, "Michael")
object2 = Object(456, "César")

table.insert(object1)
table.insert(object2)

print(table.search(123).name)
print(table.search(456).name)
table.delete(456)
print(table.search(456))