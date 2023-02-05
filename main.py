# Imports
from peewee import *
import random

# Make and connect to database
db = PostgresqlDatabase('flash-cards', user='postgres', password='12345', host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Card(BaseModel):
    # Add 2 columns: front and back
    front = CharField()
    back = CharField()

db.drop_tables([Card])
db.create_tables([Card])

# Base data to give user something to start with
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

# Make all_cards list and append data rows into it
all_cards = []
cards = Card.select()
for c in cards:
    one_card=[c.front, c.back]
    all_cards.append(one_card)

# Function to add new flash cards
def add():
    user_question = input("\nWhat would you like the question to be? ")
    user_answer = input("What is the answer to that question? ")
    # Store new card into Card table
    added_question = Card(front={user_question}, back={user_answer})
    added_question.save()
    # Append new card to all_cards list
    new_question=[user_question, user_answer]
    all_cards.append(new_question)

    print("\nYour card is added to the list!")
    print("Would you like to add another?")
    print("\nType 'another' to add 1 more.")
    print("Type 'study' if you'd like to study from all original cards & yours.")
    print("Type 'no' if you're done studying.")

    while True:
        another_card = str(input())

        if another_card.lower() == "another":
            add()
        elif another_card.lower() == "no":
            print("\nOkay, bye!")
            quit()
        elif another_card.lower() == "study":
            print("\nTime to study all flash cards...")
            study()
        else:
            print("\nThat's not one of the options.")
            print(f"Please choose 'another', 'study', or 'no'")

# Function to start study session
def study():
    # Keep track of how many correct/incorrect answers
    correct = 0
    incorrect = 0
    # Randomize flash cards per study() call
    random.shuffle(all_cards)

    print("\nTIME TO STUDY THE PERIODIC TABLE!\n")
    print(f"There are {len(all_cards)} flash cards total.")

    # Ask user how many cards they'd like to study
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
                print("\nYou can't study a negative number of cards.")
                continue
        # Exception if user does not enter an integer
        except ValueError:
            print("\nInvalid entry.")
            print(f"Please enter an integer from 1 to {len(all_cards)}")
            continue
        else:
            print(f"\nSelecting {num_cards} random flash cards...")
            break

    # Give user flash cards to study
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
    print(f"You got {correct} flash cards correct and {incorrect} wrong")
    print("\nTo review more, type 'yes'")
    print("To add your own cards, type 'add'")
    print("To end your study session, type 'quit'")

    # Let user decide what to do next
    while True:
        print("\nWhat would you like to do?")
        next_decision = str(input())

        if next_decision.lower() == "yes":
            print("\nWow, so studious!")
            study()
        elif next_decision.lower() == "quit":
            print("\nOkay, bye!")
            quit()
        elif next_decision.lower() == "add":
            print("\nTime to add more cards to this session!")
            add()
        else:
            print("\nThat's not one of the options.")
            print(f"Please choose 'yes', 'add', or 'quit'")

# Begin study session
study()

