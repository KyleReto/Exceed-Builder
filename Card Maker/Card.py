import json

class Card:

    def __init__(self):
        self.card_type = ''
        self.attack_name = ''
        self.attack_cost = ''
        self.effects = ''
        self.range = ''
        self.power = ''
        self.speed = ''
        self.guard = ''
        self.armor = ''
        self.boost_name = ''
        self.boost_cost = ''
        self.boost_effect = ''
    
    def property_to_str_if_present(self, property_name, proper_name):
        if hasattr(self, property_name):
            return f",\n   \"{proper_name}\":\"{self.__getattribute__(property_name)}\""
        else:
            return ""

    def to_json(self):

        # Add all mandatory elements
        output = ("{\n"
        f"   \"Card Type\":\"{self.card_type}\",\n"
        f"   \"Attack Name\":\"{self.attack_name}\",\n"
        f"   \"Attack Cost\":\"{self.attack_cost}\",\n"
        f"   \"Effects\":\"{self.effects}\",\n"
        f"   \"Range\":\"{self.range}\",\n"
        f"   \"Power\":\"{self.power}\",\n"
        f"   \"Speed\":\"{self.speed}\",\n"
        f"   \"Guard\":\"{self.guard}\",\n"
        f"   \"Armor\":\"{self.armor}\",\n"
        f"   \"Boost Name\":\"{self.boost_name}\",\n"
        f"   \"Boost Cost\":\"{self.boost_cost}\",\n"
        f"   \"Boost Effect\":\"{self.boost_effect}\"")

        # TODO: Add all optional elements, if present

        # Close the object and return it
        output += "\n}"
        return output