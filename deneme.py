import pymongo
from User import User


myclient = pymongo.MongoClient(
    "mongodb+srv://frknmydn:frknmydn@cluster0.uxghr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["flaskPrototype"]  # varsa kullanır yoksa oluşturur
mycollection = mydb["Users"]
user = User("furkan", "demir", "dasdasdasd", "denemedeneme")
mycollection.insert_one(user.user_json())
