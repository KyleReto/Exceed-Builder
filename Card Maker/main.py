from Card import Card

test = Card()
test.card_type = "Normal"
print(test.is_valid())
print(test.to_json())