from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# API endpoint to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# API endpoint to get a specific book
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'})
    return jsonify(book[0])

# API endpoint to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = {
        'id': request.json['id'],
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify({'message': 'Book added successfully'})

# API endpoint to update an existing book
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'})
    book[0]['title'] = request.json['title']
    book[0]['author'] = request.json['author']
    return jsonify({'message': 'Book updated successfully'})

# API endpoint to delete a book
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'})
    books.remove(book[0])
    return jsonify({'message': 'Book deleted successfully'})

# Run the API server
if __name__ == '__main__':
    app.run(debug=True)
