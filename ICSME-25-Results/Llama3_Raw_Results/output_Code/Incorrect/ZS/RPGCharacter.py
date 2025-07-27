class RPGCharacter:
    def __init__(self, name, hp, attack_power, defense, level=1):
        # Initialize character attributes
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0  # Initialize experience points

    def attack(self, other_character):
        # Calculate damage caused to the other character
        damage = max(0, self.attack_power - other_character.defense)
        # Apply damage to the other character
        other_character.hp -= damage
        # Print attack details
        print(f"{self.name} attacks {other_character.name} for {damage} damage.")

    def heal(self):
        # Calculate new health points after healing
        self.hp = min(100, self.hp + 10)
        # Return current health points
        return self.hp

    def gain_exp(self, amount):
        # Add experience points
        self.exp += amount
        # Check if character can level up
        while self.exp >= 100 * self.level and self.level < 100:
            # Level up character
            self.level_up()

    def level_up(self):
        # Increase level
        self.level += 1
        # Reset experience points
        self.exp -= 100 * (self.level - 1)
        # Increase health points, attack power, and defense
        self.hp = min(100, self.hp + 20)
        self.attack_power += 5
        self.defense += 5
        # Print level up details
        print(f"{self.name} has leveled up to level {self.level}.")
        # Return new character stats
        return self.level, self.hp, self.attack_power, self.defense

    def is_alive(self):
        # Check if character's health points are greater than 0
        return self.hp > 0


# Example usage
character1 = RPGCharacter("Player1", 100, 20, 10)
character2 = RPGCharacter("Player2", 80, 15, 8)

character1.attack(character2)
print(f"{character2.name}'s HP: {character2.hp}")

character2.heal()
print(f"{character2.name}'s HP after healing: {character2.hp}")

character1.gain_exp(500)
print(f"{character1.name}'s level: {character1.level}")
print(f"{character1.name}'s HP: {character1.hp}")
print(f"{character1.name}'s attack power: {character1.attack_power}")
print(f"{character1.name}'s defense: {character1.defense}")

print(f"Is {character1.name} alive? {character1.is_alive()}")