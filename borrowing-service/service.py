from models import db, Borrowing
from datetime import datetime
from flask import jsonify
import requests

BOOK_SERVICE_URL = 'http://localhost:5002/books'
USER_SERVICE_URL = 'http://localhost:5001/users'

class BorrowingService:
    
    @staticmethod
    def borrow_book(book_id, user_id):
        # Check if user exists
        user_response = requests.get(f"{USER_SERVICE_URL}/{user_id}")
        if user_response.status_code == 404:
            return jsonify({'message': 'User not found'}), 404

        # Check book availability from Book Service
        book_data = requests.get(f"{BOOK_SERVICE_URL}/{book_id}").json()
        if not book_data.get('is_borrowed'):
            borrowing = Borrowing(book_id=book_id, user_id=user_id, borrow_date=datetime.now())
            requests.patch(f"{BOOK_SERVICE_URL}/{book_id}", json={'is_borrowed': True})
            db.session.add(borrowing)
            db.session.commit()
            return jsonify({'message': f'Book "{book_data["title"]}" borrowed successfully'}), 200
        return jsonify({'message': 'Book is already borrowed'}), 400

    @staticmethod
    def return_book(book_id):
        borrowing = Borrowing.query.filter_by(book_id=book_id, return_date=None).first()
        if borrowing:
            borrowing.return_date = datetime.now()
            requests.patch(f"{BOOK_SERVICE_URL}/{book_id}", json={'is_borrowed': False})
            db.session.commit()
            return jsonify({'message': 'Book returned successfully'}), 200
        return jsonify({'message': 'Book was not borrowed'}), 400
