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
for c in cards:
    one_card=[c.front, c.back]
    all_cards.append(one_card)
    random.shuffle(all_cards)

def add():
    user_question = input("What would you like the question to be? ")
    user_answer = input("What is the answer to that question? ")
    added_question = Card(front={user_question}, back={user_answer})
    added_question.save()
    new_question=[user_question, user_answer]
    all_cards.append(new_question)
    random.shuffle(all_cards)
    print("Your card is added to the list!")
    while True:
        print("Would you like to add another?")
        print("Type 'another' to add 1 more.")
        print("Type 'study' if you'd like to study from all original cards & yours.")
        print("Type 'no' if you're done studying.")
        another_card = str(input())
        if another_card.lower() in "another":
            add()
        elif another_card.lower() in "no":
            print("Okay, bye!")
            quit()
        elif another_card.lower() in "study":
            print("Time to study all flash cards")
            study()
        else:
            print("That's not one of the options.")
            print(f"Please choose 'another', 'study', or 'no'")

def study():
    correct = 0
    incorrect = 0

    print("\nTIME TO STUDY THE PERIODIC TABLE!\n")
    print(f"There are {len(all_cards)} flash cards total.")

    while True:
        try:
            num_cards = int(input("\nHow many flash cards would you like to study? "))
            if (num_cards > len(all_cards)):
                print("\nThere are not that many cards.")
                print(f"Please enter an integer from 1 to {len(all_cards)}")
                continue
            elif (num_cards == 0):
                print(f"\nYou have to enter at least 1 card.")
                continue
            elif (num_cards < 0):
                print("You can't study a negative number of cards.")
                continue
        except ValueError:
            print("\nInvalid entry.")
            print(f"Please enter an integer from 1 to {len(all_cards)}")
            continue
        else:
            print(f"\nSelecting {num_cards} random flash cards...")
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

    print(f"\nYou've reviewed all {num_cards} flash cards!")
    print("\nTo review more, type 'yes'")
    print("To add your own cards, type 'add'")
    print("To end your study session, type 'quit'")

    while True:
            print("\nWhat would you like to do?")
            next_decision = str(input())

            if next_decision.lower() in "yes":
                print("Wow, so studious!")
                study()
            elif next_decision.lower() in "quit":
                print("Okay, bye!")
                quit()
            elif next_decision.lower() in "add":
                print("adding more")
                add()
            else:
                print("\nThat's not one of the options.")
                print(f"Please choose 'yes', 'add', or 'quit'")
    
study()

