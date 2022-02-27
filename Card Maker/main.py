from email.policy import default
from Card import Card

# Asks the user for input with a default value
def input_or_default(parameter_name, default_val):
    output = default_val
    user_input = input(parameter_name + f' [{default_val}]: ')
    if user_input != '':
        output = user_input
    return output

def input_required(parameter_name):
    pass

action_type = 0
while (action_type != 3):
    action_type = int(input("""Select an option:
    1. Create a New Card
    2. Edit an Existing Card
    3. Exit\n"""))
    card = Card()

    if action_type == 1:
        card.card_type = input(f"Card Type (Normal, Special, or Ultra): {card.card_type}")
        card.attack_name = input_or_default("Attack Name", 'Power')
        card.range = input("Attack Range: ")
        card.power = input("Attack Power: ")
        card.speed = input("Attack Speed: ")
        card.boost_name = input("Boost Name: ")
        card.boost_effect = input("Boost Effect: ")
        print("The following parameters are optional. Press [Enter] to skip any.")

        print(card.to_json())
    elif action_type == 2:
        # TODO: Load a card from a file
        pass
    elif action_type == 3:
        break
    else:
        print ("Invalid option, please choose a valid option.")
