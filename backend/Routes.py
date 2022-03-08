import resource
from flask_restful import Resource



class BookLIst(resource):
    def get(self):
        return {'hello': 'from booklist'}

class Book(resource):
    def get(self):
        return {'hello': 'from book'}


class ReviewList(resource):
    def get(self):
        return {'hello': 'from reviews'}


class Review(resource):
    def get(self):
        return {'hello': 'from review'}


