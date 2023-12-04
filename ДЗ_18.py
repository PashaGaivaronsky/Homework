print("Домашнее задание")
class Tomato:
    states = {1: "Только посажен", 2: "Спеет", 3: "Созрел"}
    def __init__(self, index):
        self._index = index
        self._state = self.states[1]

    def grow(self):
        if self._state == self.states[1]:
            self._state = self.states[2]
        elif self._state == self.states[2]:
            self._state = self.states[3]
        return self._state

    def is_ripe(self):
        return "Томат созрел" if self._state == self.states[3] else "Томат не созрел"


class TomatoBush:

    def __init__(self, count):
        self.tomato_grow = None
        self.tomatoes = [Tomato(1) for i in range(count)]

    def grow_all(self):
        for i in self.tomatoes:
            return i.grow()

    def all_is_ripe(self):
        for i in self.tomatoes:
            return i.is_ripe()

    def give_away_all(self):
        if tomato.is_ripe() == "Томат созрел":
            self.tomatoes.clear()

class Gardener:

    def __init__(self, name, plant: TomatoBush):
        self.name = name
        self._plant = plant

    def work(self):
        return self._plant.grow_all()

    def harvest(self):
        return "Урожай можно собирать" if self._plant.all_is_ripe() else "Урожай к сбору не готов!!!"

    @staticmethod
    def knowledge_base():
        return "Справка по садоводству"





tomato = Tomato(1)
tomato_2 = TomatoBush(5)
gardener = Gardener("Pasha", tomato_2)
print(gardener.knowledge_base())
print(gardener.work())
gardener.work()
print(gardener.harvest())




