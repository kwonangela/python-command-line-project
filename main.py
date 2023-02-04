from peewee import *
import random

db = PostgresqlDatabase('flash-cards', user='postgres', password='12345',
                        host='localhost', port=5432)
db.connect()
class BaseModel(Model):
    class Meta:
        database = db
class Card(BaseModel):
    front = CharField()
    back = CharField()
db.drop_tables([Card])
db.create_tables([Card])

hydrogen = Card(front='What is H on the periodic table?', back='Hydrogen')
hydrogen.save()
helium = Card(front='What is He on the periodic table?', back='Helium')
helium.save()
lithium = Card(front='What is Li on the periodic table?', back='Lithium')
lithium.save()
beryllium = Card(front='What is Be on the periodic table?', back='Beryllium')
beryllium.save()
boron = Card(front='What is B on the periodic table?', back='Boron')
boron.save()
carbon = Card(front='What is C on the periodic table?', back='Carbon')
carbon.save()
nitrogen = Card(front='What is N on the periodic table?', back='Nitrogen')
nitrogen.save()
oxygen = Card(front='What is O on the periodic table?', back='Oxygen')
oxygen.save()
fluorine = Card(front='What is F on the periodic table?', back='Fluorine')
fluorine.save()
neon = Card(front='What is Ne on the periodic table?', back='Neon')
neon.save()

all_cards = []
cards = Card.select()
# print (cards.sql())
for c in cards:
    # print("front: {}".format(c.front))
    # print("back: {}".format(c.back))
    one_card=[c.front, c.back]
    all_cards.append(one_card)
random.shuffle(all_cards)

correct = 0
incorrect = 0

print("\nTIME TO STUDY THE PERIODIC TABLE!\n")
print(f"There are {len(all_cards)} flash cards total.")

while True:
    try:
        num_cards = int(input("How many flash cards would you like to study? "))
    except ValueError:
        print("Invalid entry.")
        print(f"Please enter an integer from 1 to {len(all_cards)}")
        continue
    else:
        print(f"\nSelecting {num_cards} random flash cards...\n")
        break

for index in range(num_cards):
    question = all_cards[index][0]
    answer = (all_cards[index][1].lower())
    user_input = input(f"\n{question} ")
    if ((user_input.lower()) in {answer}):
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect! It is {answer.upper()}")
        incorrect += 1
    print(f"\tCorrect: {correct} Incorrect: {incorrect}")

print(f"You've reviewed all {num_cards} flash cards!")
print("If you'd like to review more, type 'yes'")
print("If you'd like to add your own cards, type 'add'")
print("Want to end your study session? Type 'quit'")
next_decision = input()

# input("Press enter to begin")
# print("f")

