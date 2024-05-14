from flask import Flask, request
from book_service import BookService

app = Flask(__name__)
book_service = BookService()

if __name__ == '__main__':
    app.run()


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    response = book_service.create_book(data)
    return str(response), 201


@app.route('/books/<bookId>', methods=['GET'])
def get_book(bookId):
    response = book_service.get_book_by_id(bookId)
    if response is None:
        return 'Book not found', 404
    return response, 200


@app.route('/books', methods=['GET'])
def get_all_books():
    # we go and get all book from DB
    return [
        {
            "id": 1,
            "kokos": True,
            "name": "Effective Python for QA",
            "pages": 120
        },
        {
            "id": 2,
            "kokos": False,
            "name": "Effective Python for Dev",
            "pages": 125
        }
    ], 200


@app.route('/books/<bookId>', methods=['PUT'])
def update_book(bookId):
    data = request.get_json()
    data["id"] = bookId
    # update book in db
    return data, 200


@app.route('/books/<bookId>', methods=['PATCH'])
def update_book_partially(bookId):
    name = request.get_json()["name"]
    # update book in db
    return {
        "id": bookId,
        "kokos": False,
        "name": name,
        "pages": 125
    }, 200


@app.route('/books/<bookId>', methods=['DELETE'])
def delete_book(bookId):
    book_service.delete_book_by_id(bookId)
    return '', 204
