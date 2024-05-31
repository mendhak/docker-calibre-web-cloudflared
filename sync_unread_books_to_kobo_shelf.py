import sqlite3

# connect to metadata.db and get the unread books

def get_unread_books():
    conn = sqlite3.connect('Books/metadata.db')
    c = conn.cursor()
    c.execute("SELECT b.id, b.title from books b left join custom_column_1 cc1 on b.id = cc1.book WHERE cc1.book is null order by b.id ASC;")
    unread_books = c.fetchall()
    conn.close()
    return unread_books

unread_books = get_unread_books()
   
# Clear the book_shelf_link table and insert the unread book IDs

conn_app = sqlite3.connect('data/app.db')
c_app = conn_app.cursor()
c_app.execute("DELETE FROM book_shelf_link WHERE shelf=1;") 
for book in unread_books:
    print(book[0], book[1])
    c_app.execute("INSERT INTO book_shelf_link (book_id, 'order', shelf, date_added) VALUES (?, 30, 1, datetime('now'));", (book[0],))
conn_app.commit()
