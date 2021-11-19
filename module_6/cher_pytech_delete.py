""" 
    Title: pytech_delete.py
    Author: Chee Her
    Date: 11/19/2021
    Description: Test program for deleting documents from the pytech collection
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

# new student to add
new_student = {
    "student_id": "1010",
    "first_name": "Gandalf",
    "last_name": "The Grey"
}

# insert the new student to MongoDB
new_student_id = students.insert_one(new_student).inserted_id

# insert statements
print("\n -- INSERT STATEMENTS --")
print("\n Inserted student record into the students collection with document_id" + str(new_student_id))

# Find the student with id 1010
student_added_doc = students.find_one({"student_id": "1010"})

# display the results 
print("\n -- DISPLAYING STUDENT TEST DOC --")
print(" Student ID: " + student_added_doc["student_id"] + "\n  First Name: " + student_added_doc["first_name"] + "\n  Last Name: " + student_added_doc["last_name"] + "\n")

# call the delete_one method to remove the student_added_doc
deleted_student_doc = students.delete_one({"student_id": "1010"})

# find all students
updated_student_list = students.find({})

# display message
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over collection of students
for doc in updated_student_list:
    print(" Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exiting message
input("\n\n  End of program, press any key to continue...")