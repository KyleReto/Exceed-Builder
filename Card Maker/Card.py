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

    def serialize(self):
        output = json.dumps(self, default=lambda o: o.__dict__, indent=4)
        return output
    
    @staticmethod
    def deserialize(json_str):
        json_obj = json.loads(json_str)
        card = Card()
        for key in json_obj:
            setattr(card, key, json_obj.get(key))
        return card
    
    def to_file(self, file_path):
        f = open(file_path, 'w')
        f.write(self.serialize())
        f.close()
    
    @staticmethod
    def from_file(file_path):
        f = open(file_path, 'r')
        card = Card.deserialize(f.read())
        f.close()
        return card