/*
    Title: whatabook.init.sql
    Author: Chee Her
    Date: 12/17/2021
    Description: WhatABook database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    start_at    TIME            NOT NULL,
    end_at      TIME            NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale, start_at, end_at)
    VALUES('12345 North Star Street, Plymouth, MN 54412', '10:00:00', '17:00:00');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Hobbit', 'J.R.Tolkien', 'About a Halfling going on an adventure');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Philosophers Stone', 'J. K. Rowling', 'A boy with wizard power');

INSERT INTO book(book_name, author, details)
    VALUES('The Little Prince', 'Antonine de Saint-Exupery', "Follows a young prince who visits various planets in space");

INSERT INTO book(book_name, author, details)
    VALUES('Dream of the Red Chamber', 'Dream of the Red Chamber', "A Chinese literatures Four Great Classical Novels");

INSERT INTO book(book_name, author, details)
    VALUES('And Then There Were None', 'Agatha Christie', "Story of ten lines of children counting rhyme");

INSERT INTO book(book_name, author, details)
    VALUES('The Lion, the Witch and the Wardrobe', 'C. S. Lewis', "Story of a mystical world in a wardrobe");

INSERT INTO book(book_name, author, details)
    VALUES('She: A History of Adventure', 'H. Rider Haggard', "The story is a first-person narrative which follows the journey of Horace Holly and his ward Leo Vincey to a lost kingdom in the African interior");

INSERT INTO book(book_name, author, details)
    VALUES('The Adventures of Pinocchio', 'Carlo Collodi', "A puppet who becomes a real boy");

INSERT INTO book(book_name, author, details)
    VALUES('The Da Vinci Code', 'Dan Brown', "A murder mystery about who the descendant of Jesus");

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('John', 'Doe');

INSERT INTO user(first_name, last_name)
    VALUES('James', 'Bond');

INSERT INTO user(first_name, last_name)
    VALUES('Katniss', 'Everdeen');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'), 
        (SELECT book_id FROM book WHERE book_name = 'The Little Prince')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'James'),
        (SELECT book_id FROM book WHERE book_name = 'The Da Vinci Code')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Katniss'),
        (SELECT book_id FROM book WHERE book_name = 'The Hobbit')
    );
