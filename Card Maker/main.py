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


action_type = 0
while (action_type != 3):
    action_type = int(input("""Select an option:
    1. Create a New Card
    2. Edit an Existing Card
    3. Exit\n"""))
    card = Card()

    if action_type == 1:
        card.card_type = input_required("Card Type (Normal, Special, or Ultra)")
        card.attack_name = input_required("Attack Name")
        card.range = input_required("Attack Range")
        card.power = input_required("Attack Power")
        card.speed = input_required("Attack Speed")
        card.boost_name = input_required("Boost Name")
        card.boost_effect = input_required("Boost Effect")
        print("The following parameters are optional. Press [Enter] to skip any.")
        # TODO: Add all optional parameters
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
