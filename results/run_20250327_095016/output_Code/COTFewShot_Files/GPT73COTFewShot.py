class RPGCharacter:
    def __init__(self, name, hp, attack_power, defense, level=1):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        damage = max(0, self.attack_power - other_character.defense)
        other_character.hp = max(0, other_character.hp - damage)

    def heal(self):
        self.hp = min(100, self.hp + 10)
        return self.hp

    def gain_exp(self, amount):
        self.exp += amount
        while self.exp >= 100 * self.level:
            self.exp -= 100 * self.level
            self.level_up()

    def level_up(self):
        if self.level < 100:
            self.level += 1
            self.hp += 20
            self.attack_power += 5
            self.defense += 5
        return self.level, self.hp, self.attack_power, self.defense

    def is_alive(self):
        return self.hp > 0