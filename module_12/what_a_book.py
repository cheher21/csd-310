""" 
    Title: what_a_book.py
    Author: Chee Her
    Date: 12/16/2021
    Description: WhatABook database in python.
"""

"""Import Statements"""
import sys
import mysql.connector
from mysql.connector import errorcode

# from logging import error
# import sys
# from mysql import connector
# import mysql.connector
# from mysql.connector import connect, errorcode
# from mysql.connector.errors import Error
# from mysql.connector.utils import validate_normalized_unicode_string


"""Config Database"""
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

"""User Interface"""

"""Show Menu"""
def show_menu():
    print("\nMain Menu")
    print("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program")

    try:
        choice = int(input("Enter a number from the menu list above from 1 - 4:     "))

        return choice
    except ValueError:
        print("\nNot a valid number.....Exit\n")

        sys.exit(0)

"""Show the Books"""
def show_books(_cursor):
    # Inner Join
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\nDisplay Book Listing")

    # Loops through the data and displays it
    for book in books:
        print("Book Name: {}\n Author: {}\nDetails {}\n".format(book[0], book[1], book[2]))

"""Shows the Store Locations"""
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\nDisplay Store Locations")

    # Loops through the stores locations and displays it
    for location in locations:
        print("Locale: {}\n".format(location[1]))
        # print("Locale: {}\n {}\nOpen Hours {}\nClosing Hours {}".format(location[1]))


"""Validates the User"""
def validate_user():
    """Validating the users ID"""

    try:
        user_id = int(input("\nEnter customer id:   "))

        if user_id < 0 or user_id > 3:
            print("\nUser ID not a valid ID...Exiting\n")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\nNot a valid number...Exiting\n")
        sys.exit(0)

"""Shows the User Account Menu Options"""
def show_account_menu():
    """Displays the users menu options"""

    try:
        print("\nCustomer Menu")
        print("1)Wishlist\n2)Add Book\n3)Main Menu")
        account_option = int(input("Enter a wishlist:   "))
        return account_option
    except ValueError:
        print("\nNot a valid number...Exiting\n")
        sys.exit(0)

"""Shows the Wishlist"""
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\nDisplay the Wishlist Items")

    for book in wishlist:
        print("Book Name: {}\n      Author: {}\n".format(book[4], book[5]))

"""Shows the books on the wishlist"""
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\nDisplays All Available Books")

    for book in books_to_add:
        print("Book ID: {}\n    Book Name: {}\n".format(book[0], book[1]))

"""Adds the book from the wishlist"""
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


try: 
    """Try and catch to handle errors"""
    # Connects to the WhatABook database
    db = mysql.connector.connect(**config)

    # Cursor for the MySQL queries
    cursor = db.cursor()

    # Displays the welcoming message
    print("\nWelcome to the WhatABook")

    # Shows the main menu to the user
    user_selection = show_menu()

    # User selection is not 4
    while user_selection != 4:

        # User selection is 1, the show book menu is be shown
        if user_selection == 1:
            show_books(cursor)

        # User selection is 2, the show locations menu is shown
        if user_selection == 2:
            show_locations(cursor)

        # User selection is 3, will validate user
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # User selection is not 3
            while account_option != 3:

                # User selection is 1, the show wishlist will be shown
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # User selection is 2
                if account_option == 2:

                    # will show the books that are not in the wishlist
                    show_books_to_add(cursor, my_user_id)

                    # Gets the book by id
                    book_id = int(input("\nEnter the id of the book you want to add:    "))

                    # Adds the book to the wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # commit to the database
                    db.commit()

                    # Displays that the book was added to the wishlist
                    print("\nBook id: {} was added to your wishlist!".format(book_id))

                # If user does not select a number less than 0 and greater than 3. Will be invalid number
                if account_option < 0 or account_option > 3:
                    print("\nNot a valid option. Please try again!")

                # Shows the user menu
                account_option = show_account_menu()

        # If the user selects a number less than 0 and greater than 4. Will be invalid number
        if user_selection < 0 or user_selection > 4:
            print("\nNot a valid option. Please try again!")

        # Show the menu
        user_selection = show_menu()

    # Displays that the program is exiting
    print("\n\nProgram Exiting....")

# Handles errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username and password are incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database is incorrect or does not exist")
    else:
        print(err)

# Closes the database
finally:
    """Closes the database"""
    db.close()