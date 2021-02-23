import sqlite3


def add_book(title, author, year, price):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO BookStore (title, author, year, price) VALUES (?, ?, ?, ?)',
                   (title, author, year, price))
    connection.commit()
    cursor.close()
    connection.close()


def update_book(title, author, year, price):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute('update BookStore set author=?,year=?,price=? where title=?',
                   (author, year, price, title))
    connection.commit()
    cursor.close()
    connection.close()
    view_all()


def delete_book(title):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute('delete from BookStore where title=?', (title, ))
    connection.commit()
    cursor.close()
    connection.close()
    view_all()


def search_book(title, author, year, price):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute('select * from BookStore where author=? or year=? or price=? or title=?',
                   (author, year, price, title))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def view_all():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute('select * from BookStore')
    connection.commit()
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
