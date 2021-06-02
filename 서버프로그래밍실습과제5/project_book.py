from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_book import Base, BookStore, BookItem

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@localhost/bookstore')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# 1. JSON return 함수 구현 할 것
@app.route('/bookstores/<int:bookstore_id>/booklist/JSON')
def bookListJSON(bookstore_id):
    bookStore = session.query(BookStore).filter_by(id=bookstore_id).one()
    bookItem = session.query(BookItem).filter_by(bookstore_id=bookstore_id)
    return bookItem

# 2. bookList 함수 구현 할 것 (booklist.html template 구축해야 함)
@app.route('/')
@app.route('/bookstores/<int:bookstore_id>/booklist')
def bookList(bookstore_id=None):
    bookStore = session.query(BookStore).filter_by(id=bookstore_id).one()
    bookItem = session.query(BookItem).filter_by(bookstore_id=bookstore_id)
    return render_template(
        'booklist.html', bookstore=bookStore, items=bookItem, bookstore_id=bookstore_id
    )


# 3. newBookItem 함수 구현 할 것 (newbook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/new', methods=['GET', 'POST'])
def newBookItem(bookstore_id):
    bookstore = session.query(BookStore).filter_by(id=bookstore_id).one()
    if request.method == 'POST':
        newItem = BookItem(name=request.form['name'], price=request.form['price'], \
        bookstore=bookstore)
        session.add(newItem)
        session.commit()
        return redirect(url_for('bookList', bookstore_id=bookstore_id))
    else:
        return render_template('newbook.html', bookstore_id=bookstore_id)


# 4. editBookItem 함수 구현 할 것 (editbook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/<int:book_id>/edit',
           methods=['GET', 'POST'])
def editBookItem(bookstore_id, book_id):
    editedItem = session.query(BookItem).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name'] and request.form['price']:
            editedItem.name = request.form['name']
            editedItem.price = request.form['price']
        session.add(editedItem)
        session.commit()
        flash("Book List has benn edited")
        #이렇게 param으로 값을 넘겨준다.
        return redirect(url_for('bookList', bookstore_id=bookstore_id))
    else:
        return render_template(
            'editbook.html', bookstore_id=bookstore_id, book_id=book_id, item=editedItem
        )


# 5. deleteBookItem 함수 구현 할 것 (deletebook.html template 구축해야 함)
@app.route('/bookstores/<int:bookstore_id>/<int:book_id>/delete',
           methods=['GET', 'POST'])
def deleteBookItem(bookstore_id, book_id):
    itemToDelete = session.query(BookItem).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Book List has been deleted")
        return redirect(url_for('bookList', bookstore_id=bookstore_id))
    else:
        return render_template('deletebookitem.html', bookstore_id=bookstore_id, item=itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
