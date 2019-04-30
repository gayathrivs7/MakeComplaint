from dbfile import db,Puppy

#create

my_puppy = Puppy('Rufus',5,"german shepard","black")
db.session.add(my_puppy)
db.session.commit()

#Read
print("=========================================")
all_puppies = Puppy.query.all()
print("\n\nListing all Puppies\n")
print(all_puppies)
print("=========================================")


#Select by id

puppy_one  = Puppy.query.get(1)
print("\nPrinting Puppy name with id 1\n")
print(puppy_one.name)
print("=========================================")

#Filters

puppy_frankie  =  Puppy.query.filter_by(name = 'Frankie')
print("\n\nDetails of Frankie Puppy\n")
print(puppy_frankie.all())
print("=========================================")

#Update

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()
 

all_puppies = Puppy.query.all()
print("\n\nListing all Puppies aftr upadting value of first puppy\n")
print(all_puppies)
print("=========================================")


db.session.commit()


