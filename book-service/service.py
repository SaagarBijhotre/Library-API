# book-service/service.py

from flask import jsonify
from models import db, Book

class BookService:

    @staticmethod
    def add_book(data):
        # Handle adding a new book
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'}), 201

    @staticmethod
    def check_availability(book_id):
        # Check if a book is available
        book = Book.query.get(book_id)
        if book and not book.is_borrowed:
            return jsonify({'id': book.id, 'title': book.title, 'is_borrowed': book.is_borrowed}), 200
        elif book and book.is_borrowed:
            return jsonify({'message': 'Book is already borrowed'}), 400
        return jsonify({'message': 'Book not found'}), 404
