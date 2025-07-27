class RPGCharacter:
    """
    The class represents a role-playing game character, which allows to attack other characters, heal, gain experience, level up, and check if the character is alive.
    """

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        :param name: str, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    # Method to attack another character
    def attack(self, other_character):
        # Calculate the damage caused to the other character
        damage = max(self.attack_power - other_character.defense, 0)
        # Subtract the damage from the other character's health points
        other_character.hp -= damage

    # Method to heal the character
    def heal(self):
        # Calculate the new health points after healing
        self.hp = min(self.hp + 10, 100)
        # Return the current health points
        return self.hp

    # Method to gain experience points
    def gain_exp(self, amount):
        # Add the experience points to the character's current experience
        self.exp += amount
        # Level up the character if the experience points are sufficient
        while self.exp >= 100 * self.level and self.level < 100:
            self.level_up()

    # Method to level up the character
    def level_up(self):
        # Increase the character's level
        self.level += 1
        # Reset the character's experience points
        self.exp -= 100 * (self.level - 1)
        # Increase the character's health points, attack power, and defense points
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
        # Return the new level, health points, attack power, and defense points
        return self.level, self.hp, self.attack_power, self.defense

    # Method to check if the character is alive
    def is_alive(self):
        # Return True if the character's health points are greater than 0, False otherwise
        return self.hp > 0