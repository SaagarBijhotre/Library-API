from flask import Blueprint, request, jsonify
from models import db, Book

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@book_routes.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [{'id': book.id, 'title': book.title, 'author': book.author, 'is_borrowed': book.is_borrowed} for book in books]
    return jsonify(books_list)
