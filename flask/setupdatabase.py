from db import d,Puppy

#creates all the tables model
d.create_all()

sam   = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)
print(frank.id)

d.session.add_all([sam,frank])
d.session.commit()

print(sam.id)
print(frank.id)



