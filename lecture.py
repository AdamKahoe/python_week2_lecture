import random

print(round(random.random() * 50))

def bananas():
    bananas = round(random.random() * 50)
    if bananas % 2 == 0:
        print(f"you have an even number of bananas and how many bananas {bananas}")
    return bananas

print(bananas())

pets = {
    'dog': 'Freddy',
    'cat': 'Tom',
    'hamster': 'Bingo'
}

print(pets['cat'])
pets['bird'] = "Whistles"
print(pets)
# pets['cat'] = ["Tommy", "Tom"]

for pet in pets:
    print(pets[pet])

for key in pets:
    print(key)

for pet in pets.keys():
    print(pet)
('dog', 'cat', 'hamster')

for pet in pets.values():
    print(pet)

# (('dog', 'Freddy'), ('cat', 'Tom') 'hamster')

