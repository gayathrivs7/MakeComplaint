from dbfile import db,Users

 #create table model
db.create_all()

us1 = Users(1,'Krishna','krishna007','krishna@gmail.com','password')
db.session.add(us1)
db.session.commit()
  
alls = Users.query.all()
print("\n\n All Data\n")
print(alls)
