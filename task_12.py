class Dessert:
    def __init__(self, name = None, calories = None):
        self.name = name
        self.calories = calories
    def setName(self, name):
        self.name = name
    def setCalories(self, calories):
        self.calories = calories
    def getName(self):
        return self.name
    def getCalories(self):
        return self.calories
    def is_healthy(self):
        if type(self.calories) == int or type(self.calories) == float:
            return self.calories < 200
        else:
            return False

class JellyBean(Dessert):
    def __init__(self, *args, flavor = None):
        Dessert.__init__(self, *args)
        self.flavor = flavor
    def setFlavor(self, flavor):
        self.flavor = flavor
    def getFlavor(self):
        return self.flavor
    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True