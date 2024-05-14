from pymongo import MongoClient
from pymongo.server_api import ServerApi

from book_model import Book
import uuid


def generate_random_id():
    return str(uuid.uuid4())


class BookService:
    def __init__(self):
        uri = "mongodb+srv://admin:<password>@playground.kfaprug.mongodb.net/?retryWrites=true&w=majority&appName=playground"
        self.client = MongoClient(uri,  server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("You successfully connected to MongoDB!")
        except Exception as e:
            print("Failed to connect to to MongoDB!")
            print(e)
        self.db = self.client['bookstore']
        self.collection = self.db['books']

    def create_book(self, data):
        book = Book(data["name"], data["pages"], data["author"], generate_random_id())
        result = self.collection.insert_one(book.__dict__).inserted_id
        return result

    def get_book_by_id(self, bookId):
        book = self.collection.find_one({"_id": bookId})
        return Book(**book).to_dict() if book else None

