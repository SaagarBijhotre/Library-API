from flask import Blueprint, request, jsonify
from models import db, Borrowing
from datetime import datetime
import requests

borrow_routes = Blueprint('borrow_routes', __name__)

BOOK_SERVICE_URL = 'http://localhost:5002/books'

@borrow_routes.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    # Check book availability from the Book Service
    book_data = requests.get(f"{BOOK_SERVICE_URL}/{book_id}").json()
    if not book_data.get('is_borrowed'):
        borrowing = Borrowing(book_id=book_id, user_id=request.json['user_id'], borrow_date=datetime.now())
        requests.patch(f"{BOOK_SERVICE_URL}/{book_id}", json={'is_borrowed': True})
        db.session.add(borrowing)
        db.session.commit()
        return jsonify({'message': f'Book "{book_data["title"]}" borrowed successfully'})
    return jsonify({'message': 'Book is already borrowed'}), 400

@borrow_routes.route('/return/<int:book_id>', methods=['POST'])
def return_book(book_id):
    borrowing = Borrowing.query.filter_by(book_id=book_id, return_date=None).first()
    if borrowing:
        borrowing.return_date = datetime.now()
        requests.patch(f"{BOOK_SERVICE_URL}/{book_id}", json={'is_borrowed': False})
        db.session.commit()
        return jsonify({'message': 'Book returned successfully'})
    return jsonify({'message': 'Book was not borrowed'}), 400
