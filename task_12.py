class JellyBean:
    def __init__(self, flavor = 'Some'):
        self.flavor = flavor
    def setFlavor(self, flavor):
        self.flavor = flavor
    def getFlavor(self):
        return self.flavor

class Dessert(JellyBean):
    def __init__(self, *args, name = 'Noname', cal = None):
        JellyBean.__init__(self, *args)
        self.name = name
        self.cal = cal
    def setName(self, name):
        self.name = name
    def setCal(self, cal):
        self.cal = cal
    def getName(self):
        return self.name
    def getCal(self):
        return self.cal
    def is_healthy(self):
        if self.cal == None:
            return 'CaloriesNotDetermined'
        else:
            return self.cal < 200
    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True