# 1. Entity

class X:
    def __init__(self):
        pass

# 2. Inheritance 
class Y(X):
    def __init__(self, ...):
        super.__int__(...)

# 3. Manager 
class System:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def find(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None 

# 4. Business Operation 

def perform_operation(...):

    entity = find(...)

    if entity is None:
        return False

    if invalid:
        return False

    # update state 
    return True 