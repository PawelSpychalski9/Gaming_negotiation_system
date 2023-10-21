import random
import openai
import os

#OpenAI API key
openai.api_key = "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"



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
        print(f"{i}) Potion {i}: {potion}")

    print("---------------------------------------------")
    print("\n \n \n")

def negotiatios(c1, c2, context_conversation, product):
    print("Well then, let's start negotiating the price")
    print("\033[90mNow you can type the first message that will start the negotiation\033[0m \n")
    for i in range(5):
        messaage = input("You: ")
        context_conversation += "Customer: " + messaage + "\n"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Take on the role of a concoction seller who sells such a product: {product}, your customer wants to negotiate with you earlier as part of the player's skill assessment two suggestions arose that you should consider: suggestion1 {c1}. suggestion2 {c2}. For each time we will had given the dialogue, set yourself a percentage based on these conditions below which you do not want to go and stick to it, remember that it can not be too low and to take into account the previously described conditions. Also, don't be too submissive with the player if he doesn't give any reasons to lower the price tell him you won't do it but be still open to negotiation. "
                },
                {
                    "role": "user",
                    "content": context_conversation
                }
            ],
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response_text = response.choices[0].message['content']  # Pobierz tekst odpowiedzi
        context_conversation += response_text
        print(response_text)

# Creating potion instances
potion1 = Potion(price=10, healing_points=20)
potion2 = Potion(price=15, healing_points=35)
potion3 = Potion(price=25, healing_points=50)

potion_dict = {
    "potion1": potion1,
    "potion2": potion2,
    "potion3": potion3
}


# Creating instances of the merchant and player
merchant = Merchant()
player = Player()

print("\nWelcome to the game! Your stats are:")
print(player)
print(f"\nYou interact with a merchant with the following stats:\n{merchant}")

# Calling the price_list function
price_list(potion_dict.values())
condition_1 = "Your customer is smarter than you and has better negotiating skills. You should be"


#conditions analys
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


if player.strength > merchant.assertiveness:
    if player.strength - merchant.assertiveness >= 2:
        condition_2 = "The buyer is stronger, and you should feel fear if they decide to intimidate you and willingly agree to a lower price."
    else:
        condition_2 = "The buyer is slightly stronger than you, so out of concern, you should still lower the price slightly."
else:
    condition_2 = "There is no reason to lower the price based on the player's strength, consider only the previous circumstances."

#potion choice
while True:
    choice = input("podaj numer produktu który Cię interesuje: ")
    choice = f"potion{choice}"

    if choice in potion_dict:
        print(f"you have chosen: {choice}")
        chosen_potion = potion_dict[choice]
        break

    else:
        print("No such product exists, try again")



#print potion data
print(chosen_potion)
print(f"Your balance is {player.balance}$")

context_conversation = ""

negotiation_choice = input("\033[31m [!] Do you want to negotiate the price? [Y/N]: \033[0m")
if negotiation_choice == "Y" or negotiation_choice == "y":
    negotiatios(condition_1, condition_2, context_conversation, chosen_potion)