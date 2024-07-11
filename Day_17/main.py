class User:
   def __init__(self,user_id,username,pet):
      self.id = user_id
      self.username = username
      self.pet=pet
      self.followers = 0
      self.following = 0

   def follow(self,user):
    user.followers +=1
    self.following +=1

class Car:
   def __init__(self,seats,doors):
      self.seats = seats
      self.doors = doors




toyota = Car(4,2)

user_1 = User("0001","Samuel Riedel","Wolfie")
user_2 = User("0002","Samuelooo Riedelooooo","Wolfieooooo")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)




