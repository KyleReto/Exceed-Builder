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

    def is_valid(self):
        for prop in self.__dict__:
            if self.__getattribute__(prop) == '':
                return False
        return True

    def to_json(self):

        if not self.is_valid():
            raise RuntimeError("Card is missing one or more default properties")

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
        # TODO: this lol

        # Close the object and return it
        output += "\n}"
        return output