from flask import Blueprint, request, jsonify
from models import db, Borrowing
from datetime import datetime
from service import BorrowingService

borrow_routes = Blueprint('borrow_routes', __name__)

@borrow_routes.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    user_id = request.json.get('user_id')
    result = BorrowingService.borrow_book(book_id, user_id)  # Call to the service layer
    return result

@borrow_routes.route('/return/<int:book_id>', methods=['POST'])
def return_book(book_id):
    result = BorrowingService.return_book(book_id)  # Call to the service layer
    return result