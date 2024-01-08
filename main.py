class CharShell:
    # template shell for the playable character
    def __init__(self, name, ele, path, stat, energy, counter):
        self.name = name
        self.element = ele
        self.path = path
        self.health = stat['HP']
        self.attack = stat['ATK']
        self.defense = stat['DEF']
        self.speed = stat['SPD']
        self.ult = energy
        self.counter = counter


class EnemyShell:
    # template shell for the enemy units
    def __init__(self, name, weakness, moves, stat):
        self.name = name
        self.weakness = weakness
        self.moves = moves
        self.health = stat['HP']
        self.attack = stat['ATK']
        self.defense = stat['DEF']
        self.speed = stat['SPD']


charStat = {'HP': 10, 'ATK': 5, 'DEF': 3, 'SPD': 100}
testChar = CharShell("Test", "Fire", "Preservation", charStat, 100, 0)

enemyStat = {'HP': 10, 'ATK': 5, 'DEF': 3, 'SPD': 100}
testEnemy = EnemyShell("Test", "Fire", "none", enemyStat)


def fight(char, enemy):
    print('BATTLE STARTED')
    print(f"\n{char.name}")
    print("Element:", char.element)
    print("Path:", char.path)
    print("HP:", char.health)
    print("ATK:", char.attack)
    print("DEF:", char.defense)
    print("SPD:", char.speed)
    print("Ultimate:", char.ult)
    print("Counter:", char.counter)


fight(testChar, testEnemy)

