#import flask si we can use it 
from flask import Flask, request
#this is how we manipulate the database
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#add our database
#there are several database software suites/sever you can use...MYSQL, PostresSQL, SQLserver
#the most common into level - squile... just a file that acts like a database
#config our DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#route decorator is a way for us to tie a route (url endpoint) to a function
#the route decorator (in the background) is grabbing the url and parsing it to something python can understand
#the function defined after the route then runs using the route as an endpoint

#route will take in one argument?param and that is the url path you wish to create
#if you just use a / that means the index page or home page

@app.route('/')
def home():
    return "Hello, Flask!"

#now we need to create tables for our DB...
#we can do this through models
#models are representations on how a database should look and what field/columns it should have
#this sounds familiar - class
class Book(db.Model):
    #setup our db kind of similar to how we would in sql with a couple of changes
    #we list out data fields / columns and data types and any parms needed
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author": self.author,
            "publisher": self.publisher
        }
with app.app_context():
    db.create_all()

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author=data['author'],
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Get a specific book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

# Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    db.session.commit()
    return jsonify(book.to_dict())

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)