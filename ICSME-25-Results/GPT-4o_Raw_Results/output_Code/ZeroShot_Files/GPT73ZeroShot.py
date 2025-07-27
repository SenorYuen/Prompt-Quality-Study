class RPGCharacter:
    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        """
        self.name = name
        self.hp = hp
        self.max_hp = 100
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        """
        damage = self.attack_power - other_character.defense
        if damage > 0:
            other_character.hp -= damage
        return other_character.hp

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        """
        self.hp += 10
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the value that is 100 times the current level.
        The experience that overflows should be used to calculate the next level up until exhausted.
        """
        self.exp += amount
        while self.exp >= 100 * self.level and self.level < 100:
            self.exp -= 100 * self.level
            self.level_up()

    def level_up(self):
        """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        Max level is 100.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        """
        if self.level < 100:
            self.level += 1
            self.hp += 20
            self.attack_power += 5
            self.defense += 5
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.exp = 0
        return self.level, self.hp, self.attack_power, self.defense

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        return self.hp > 0