from email.policy import default
from Card import Card

# Asks the user for input with a default value.
def input_or_default(parameter_name, default_val):
    output = default_val
    user_input = input(parameter_name + f' [{default_val}]: ')
    if user_input != '':
        output = user_input
    return output

# Asks the user for a required input
def input_required(parameter_name):
    while(True):
        user_input = input(parameter_name + ': ')
        if user_input != '':
            return user_input
        print('This field is required.')

# Asks the user for an optional input
def input_optional(parameter_name):
    return input(parameter_name + ' [None]: ')

action_type = 0
TEMP_PATH = 'Card Maker/temp.json'

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
        card.to_file(TEMP_PATH)
        card.attack_name = input_required("Attack Name")
        card.to_file(TEMP_PATH)
        print("Costs are written as #F or #G, for Force or Gauge costs. Ex. '4G' is 4 Gauge, while 1F is 1 Force.")
        card.attack_cost = input_optional("Attack Cost")
        card.to_file(TEMP_PATH)
        card.effects = input_optional("Attack Effects")
        card.to_file(TEMP_PATH)
        print("Range is written as it would be on the card. Ex. '1', '2-3', 'X', and 'N/A' are all valid.")
        card.range = input_required("Attack Range")
        card.to_file(TEMP_PATH)
        card.power = input_required("Attack Power")
        card.to_file(TEMP_PATH)
        card.speed = input_required("Attack Speed")
        card.to_file(TEMP_PATH)
        card.armor = input_optional("Attack Armor")
        card.to_file(TEMP_PATH)
        card.guard = input_optional("Attack Guard")
        card.to_file(TEMP_PATH)
        card.boost_name = input_required("Boost Name")
        card.to_file(TEMP_PATH)
        print("Boost costs are written the same as attack costs, as #F or #G.")
        card.boost_cost = input_optional("Boost Cost")
        card.to_file(TEMP_PATH)
        card.boost_effect = input_required("Boost Effect")
        card.to_file(TEMP_PATH)
        
        # TODO: Add file output
        # TODO: Add export functionality
        print(card.serialize())
    elif action_type == 2:
        card = Card.from_file(input_required("Enter the file path of the card to edit"))
        print("Change any of the card's stats. Press enter to use the old/default value, denoted in [brackets] where present.")
        card.card_type = input_or_default("Card Type (Normal, Special, or Ultra)", card.card_type)
        card.to_file(TEMP_PATH)
        card.attack_name = input_or_default("Attack Name", card.attack_name)
        card.to_file(TEMP_PATH)
        print("Costs are written as #F or #G, for Force or Gauge costs. Ex. '4G' is 4 Gauge, while 1F is 1 Force.")
        card.attack_cost = input_or_default("Attack Cost", card.attack_cost)
        card.to_file(TEMP_PATH)
        card.effects = input_or_default("Attack Effects", card.effects)
        card.to_file(TEMP_PATH)
        print("Range is written as it would be on the card. Ex. '1', '2-3', 'X', and 'N/A' are all valid.")
        card.range = input_or_default("Attack Range", card.range)
        card.to_file(TEMP_PATH)
        card.power = input_or_default("Attack Power", card.power)
        card.to_file(TEMP_PATH)
        card.speed = input_or_default("Attack Speed", card.speed)
        card.to_file(TEMP_PATH)
        card.armor = input_or_default("Attack Armor", card.armor)
        card.to_file(TEMP_PATH)
        card.guard = input_or_default("Attack Guard", card.guard)
        card.to_file(TEMP_PATH)
        card.boost_name = input_or_default("Boost Name", card.boost_name)
        card.to_file(TEMP_PATH)
        print("Boost costs are written the same as attack costs, as #F or #G.")
        card.boost_cost = input_or_default("Boost Cost", card.boost_cost)
        card.to_file(TEMP_PATH)
        card.boost_effect = input_or_default("Boost Effect", card.boost_effect)
        card.to_file(TEMP_PATH)
    elif action_type == 3:
        break
    else:
        print ("Invalid option, please choose a valid option.")
