class Dessert:
    def __init__(self, name = 'Noname', calories = None):
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
    def is_delicious(self):
        return True