import json

class Card:

    def __init__(self):
        self.card_type = ''
        self.attack_name = ''
        self.range = ''
        self.power = ''
        self.speed = ''
        self.boost_name = ''
        self.boost_effect = ''

    def to_json(self):
        # Add all mandatory elements
        output = ("{\n"
        f"   \"Card Type\":\"{self.card_type}\",\n"
        f"   \"Attack Name\":\"{self.attack_name}\",\n"
        f"   \"Range\":\"{self.range}\",\n"
        f"   \"Power\":\"{self.power}\",\n"
        f"   \"Speed\":\"{self.speed}\",\n"
        f"   \"Boost Name\":\"{self.boost_name}\",\n"
        f"   \"Boost Effect\":\"{self.boost_effect}\"")

        # Add all optional elements, if present


        # Close the object and return it
        output += "}"
        return output