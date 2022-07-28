class Dessert:
    def __init__(self, name = 'Noname', cal = None):
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
        if self.cal == None:
            return 'CaloriesNotDetermined'
        else:
            return self.cal >= 200