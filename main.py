from peewee import *

db = PostgresqlDatabase('flash-cards', user='postgres', password='',
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

banana = Card.get(Card.back=='Neon')
print(f"{banana.back} answers {banana.front}")