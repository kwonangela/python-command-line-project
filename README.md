# Periodic Table Flash Cards (Python Command Line Project)
This project is a periodic table flash card simulation via the command line. It includes a base set of data that is stored into a "card" table of a database called "flash-cards". The "card" table consists of 2 columns: "front" and "back", which represents the front and back of a flash card. A user can study from the original set of flash cards, choosing how many cards they would like to review, while keeping track of how many they get correct and incorrect. 

Once a user finishes reviewing the number of cards they chose, they can: review the original set of cards again in a new random order, stop their study session, or add more cards to the current study session. They can continue to add 1 card at a time and choose to either: study from the original set of cards and their newly added cards or end the study session. 

## PeeWee
This program uses the Python ORM, PeeWee, to connect to a PSQL database, create a model for the data, and manipulate the data.

## Installations and Reminders
- Install: `pipenv install peewee psycopg2-binary autopep8`
- To start virtual environment: `pipenv shell`
- To run file once in shell: `python3 main.py` 
- To interact with "flash-cards" database: `psql -d flash-cards`
- To view data in "card" table: `SELECT * FROM card;`

## Screenshots
- Prompts user to enter how many cards they would like to study and keeps asking if user enters invalid input:
<img width="373" alt="Screenshot 2023-02-04 at 9 50 54 PM" src="https://user-images.githubusercontent.com/117434437/216799135-1c7c7d0a-11d3-469e-a696-24b5197dc7d7.png">

- Keeps track of correct and incorrect answers (not case-sensitive) and asks user what they would like to do after they go through the cards:
<img width="373" alt="Screenshot 2023-02-04 at 9 51 41 PM" src="https://user-images.githubusercontent.com/117434437/216799137-e251ef57-c131-4375-b5ba-ccb1197165b0.png">

- Keeps asking user what their next step is until they enter a valid choice. If user responds ‘yes’, the study session resets, asking again how many cards they want to choose, and producing questions in another random order:
<img width="359" alt="Screenshot 2023-02-04 at 9 52 51 PM" src="https://user-images.githubusercontent.com/117434437/216799139-a48fd390-a65c-4dbb-bb20-1943bf528faf.png">

- If user wants to add a new flash card, the program prompts user to enter the question (“front”) and answer (“back”). This new flash card is then stored into the database. After, user can add another question, study from the current list of questions, or end the program:
<img width="533" alt="Screenshot 2023-02-04 at 9 54 06 PM" src="https://user-images.githubusercontent.com/117434437/216799144-94b92028-215d-4e26-a63c-52a622c2b4e5.png">

- Shows that the new question is added into the list:
<img width="322" alt="Screenshot 2023-02-04 at 9 54 57 PM" src="https://user-images.githubusercontent.com/117434437/216799147-6b44c0b1-4d1a-4acd-bcf0-9081352fa4a4.png">

- Quits program once user types “quit”:
<img width="315" alt="Screenshot 2023-02-04 at 9 55 23 PM" src="https://user-images.githubusercontent.com/117434437/216799148-c301a564-8a84-41ea-a96e-0a3a48959163.png">

- Shows that the new question is stored into the database:
<img width="459" alt="Screenshot 2023-02-04 at 9 56 38 PM" src="https://user-images.githubusercontent.com/117434437/216799163-9807c53a-0a9b-4ea4-9185-7efb70b04028.png">







