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
    while(True):
        user_input = input(parameter_name + ': ')
        if user_input != '':
            return user_input
        print('This field is required.')

def input_optional(parameter_name):
    return input(parameter_name + ' [None]: ')

action_type = 0
while (action_type != 3):
    try:
        action_type = int(input("""Select an option:
        1. Create a New Card
        2. Edit an Existing Card
        3. Exit\n"""))
    except ValueError:
        pass
    card = Card()

    if action_type == 1:
        print("Set the card's stats. Press enter to use the default value, denoted in [brackets] where present.")
        card.card_type = input_required("Card Type (Normal, Special, or Ultra)")
        card.attack_name = input_required("Attack Name")
        print("Costs are written as #F or #G, for Force or Gauge costs. Ex. '4G' is 4 Gauge, while 1F is 1 Force.")
        card.attack_cost = input_optional("Attack Cost")
        card.effects = input_optional("Attack Effects")
        print("Range is written as it would be on the card. Ex. '1', '2-3', 'X', and 'N/A' are all valid.")
        card.range = input_required("Attack Range")
        card.power = input_required("Attack Power")
        card.speed = input_required("Attack Speed")
        card.guard = input_optional("Attack Guard")
        card.armor = input_optional("Attack Armor")
        card.boost_name = input_required("Boost Name")
        print("Boost costs are written the same as attack costs, as #F or #G.")
        card.boost_cost = input_optional("Boost Cost")
        card.boost_effect = input_required("Boost Effect")
        
        # TODO: Add file output
        # TODO: Add export functionality
        print(card.to_json())
    elif action_type == 2:
        # TODO: Load a card from a file
        pass
    elif action_type == 3:
        break
    else:
        print ("Invalid option, please choose a valid option.")
