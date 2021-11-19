""" 
    Title: pytech_update.py
    Author: Chee Her
    Date: 11/19/2021
    Description: Test program for updating a document in the pytech collection
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.c9khq.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to MongoDB
client = MongoClient(url)

# gets the pytech from the database
db = client.pytech

# gets the student collection
students = db.students

# finds all the student in the pytech collection
student_list = students.find({})

# displays the desplayed student
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop through collection
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# update student
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakkenshield Son of Thrain"}})

# find the student that was updated
thorin = students.find_one({"student_id": "1007"})

# display the student that was updated
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# display the updated student info
print("  Student ID: " + thorin["student_id"] + "\n First Name: " + thorin["first_name"] + "\n Last Name: " + thorin["last_name"] + "\n")

# exit message
input("\n\n End of program, press any key to continue...")