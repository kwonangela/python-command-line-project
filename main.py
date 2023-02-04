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
print (cards.sql())
for c in cards:
    print("front: {}".format(c.front))
    print("back: {}".format(c.back))
    one_card=[c.front, c.back]
    all_cards.append(one_card)
random.shuffle(all_cards)

correct = 0
incorrect = 0

print("\nTime to study your periodic table!\n")
for index in range(len(all_cards)):
    question = all_cards[index][0]
    answer = all_cards[index][1]
    user_input = input(question)
    if (user_input in {answer}):
        print("Correct!")

# input("Press enter to begin")
# print("f")

