from dbfile import Puppy, db
import sqlalchemy


#creates all the tables model
db.create_all()

sam   = Puppy('Sammy',3,"dashunt","brownade")
frank = Puppy('Frankie',4,"lab","white")

print(sam.id)
print(frank.id)

db.session.add(sam)

db.session.add(frank)
db.session.commit()

print(sam.id)
print(frank.id)





