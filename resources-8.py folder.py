# Save this code in resources.py

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


# Existing player1 character
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

# Profile for Dragon Slayer
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

# Adding your own character (replace 'YourName' with your actual name)
player2 = Character('Lela-Parks', ['rope', 'pen', 'paper', 'idea'], ['small', 'confusion'])

# Profile for your character
for item in player2.weapons:
    print("Item: ", item)
for debuff in player2.weaknesses:
    print("Debuff: ", debuff)
