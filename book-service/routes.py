from flask import Blueprint, request, jsonify
from service import BookService
from models import db, Book

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    return BookService.add_book(data)

@book_routes.route('/books', methods=['GET'])
def check_availability():
    books = Book.query.all()
    return BookService.check_availability(book_id)