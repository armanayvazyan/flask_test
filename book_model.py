class Book:
    def __init__(self, name, pages, author, _id=None):
        self._id = _id
        self.pages = pages
        self.name = name
        self.author = author

    def to_dict(self):
        return {
            '_id': self._id,
            'pages': self.pages,
            'title': self.name,
            'author': self.author
        }