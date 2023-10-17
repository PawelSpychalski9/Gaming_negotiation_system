import random

class Player:
    def __init__(self):
        self.balance = 35  # Initial balance is $35
        self.hp = random.randint(1, 100)  # Random HP value from 1 to 100
        self.strength = random.randint(1, 10)  # Random strength value from 1 to 10
        self.intelligence = random.randint(1, 10)  # Random intelligence value from 1 to 10

    def __str__(self):
        return f"Balance: ${self.balance}, HP: {self.hp}, Strength: {self.strength}, Intelligence: {self.intelligence}"

class Merchant:
    def __init__(self):
        self.vulnerability = random.randint(1, 6)  # Random vulnerability value from 1 to 6
        self.assertiveness = random.randint(1, 10)  # Random assertiveness value from 1 to 10

    def __str__(self):
        return f"Vulnerability: {self.vulnerability}, Assertiveness: {self.assertiveness}"

class Potion:
    def __init__(self, price, healing_points):
        self.price = price
        self.healing_points = healing_points

    def __str__(self):
        return f"Price: ${self.price}, Healing Points: {self.healing_points}"

def price_list(potions):
    print("\n \n \n--------========+|  Price List  |+========--------")
    for i, potion in enumerate(potions, 1):
        print(f"Potion {i}: {potion}")

    print("---------------------------------------------")
    print("\n \n \n")

# Creating potion instances
potion1 = Potion(price=10, healing_points=20)
potion2 = Potion(price=15, healing_points=35)
potion3 = Potion(price=25, healing_points=50)

# List of potions
potions = [potion1, potion2, potion3]

# Creating instances of the merchant and player
merchant = Merchant()
player = Player()

print("\nWelcome to the game! Your stats are:")
print(player)
print(f"\nYou interact with a merchant with the following stats:\n{merchant}")

# Calling the price_list function
price_list(potions)
condition_1 = "Your customer is smarter than you and has better negotiating skills. You should be"

if player.intelligence >= merchant.vulnerability:
    if player.intelligence - merchant.vulnerability >= 3:
        condition_1 += " able to sell your potions for a much lower price."
    elif player.intelligence - merchant.vulnerability >= 2:
        condition_1 += " able to sell your potions for a lower price."
    else:
        condition_1 += " able to sell your potions for a slightly lower price."
else:
    if merchant.vulnerability - player.intelligence >= 3:
        condition_1 += " able to sell your potions for a much higher price."
    elif merchant.vulnerability - player.intelligence >= 2:
        condition_1 = "be minimally bent on negotiation"
    else:
        condition_1 = "sell for regular price"

print(condition_1)

condition_2 = "."
if player.strength > merchant.assertiveness:
    if player.strength - merchant.assertiveness >= 2:
        condition_2 = "The buyer is stronger, and you should feel fear if they decide to intimidate you and willingly agree to a lower price."
    else:
        condition_2 = "The buyer is slightly stronger than you, so out of concern, you should still lower the price slightly."
else:
    condition_2 = "There is no reason to lower the price based on the player's strength, consider only the previous circumstances."

x= 1