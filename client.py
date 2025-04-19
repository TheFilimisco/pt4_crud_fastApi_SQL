import requests
authors_url = "http://127.0.0.1:8000/authors"
genres_url = "http://127.0.0.1:8000/genres"
books_url = "http://127.0.0.1:8000/books"

#Authors
def read_authors():
    data = requests.get(f"{authors_url}")
    print(data.status_code)
    for author in data.json():
        print(author)

def read_author(author_id: int):
    data = requests.get(f"{authors_url}/{author_id}")
    print(data.status_code)
    print(data.json())

def create_author():
    author = {
    "name": "Gabriel Garcia Marquez",
    "age": 45,
    "description": "Is a writter from Colombia"}
    data = requests.post(f"{authors_url}", json=author)
    print(data.status_code)
    print(data.json())

def update_author(author_id: int):
    author_update = {
    "name": "Gabriel Garcia Marquez X2",
    "age": 49,
    "description": "Is a writter from Colombia that he..."
    }
    data = requests.patch(f"{authors_url}/{author_id}", json=author_update)
    print(data.status_code)
    print(data.json())

def delete_author(author_id: int):
    data = requests.delete(f"{authors_url}/{author_id}")
    print(data.status_code)
    print(data.json())

#Genres
def read_genres():
    data = requests.get(f"{genres_url}")
    print(data.status_code)
    for genre in data.json():
        print(genre)

def read_genre(genre_id: int):
    data = requests.get(f"{genres_url}/{genre_id}")
    print(data.status_code)
    print(data.json())

def create_genre():
    genre = {
    "name": "Fantasy",
    "description": "A genre about magic"}
    data = requests.post(f"{genres_url}", json=genre)
    print(data.status_code)
    print(data.json())

def update_genre(genre_id):
    genre_update = {
    "name": "Fantasy2",
    "description": "A genre about magic2"}
    data = requests.patch(f"{genres_url}/{genre_id}", json=genre_update)
    print(data.status_code)
    print(data.json())

def delete_genre(genre_id: int):
    data = requests.delete(f"{genres_url}/{genre_id}")
    print(data.status_code)
    print(data.json())

# Books
def read_books():
    data = requests.get(f"{books_url}")
    print(data.status_code)
    for book in data.json():
        print(book)

def read_book(book_id: int):
    data = requests.get(f"{books_url}/{book_id}")
    print(data.status_code)
    print(data.json())

def create_book():
    book = {
    "title": "Harry Potter and the Philosopher's Stone",
    "description": "A boy magic",
    "rating": 8,
    "author_id": 3}
    data = requests.post(f"{books_url}", json=book)
    print(data.status_code)
    print(data.json())

def update_book(book_id):
    book_update = {
    "title": "harry potter and the prisoner of azkaban",
    "description": "A boy magic",
    "rating": 8,
    "author_id": 3}
    data = requests.patch(f"{books_url}/{book_id}", json=book_update)
    print(data.status_code)
    print(data.json())

def delete_book(book_id):
    data = requests.delete(f"{books_url}/{book_id}")
    print(data.status_code)
    print(data.json())

#

if __name__ == "__main__":
    print("Authors")
    read_authors()
    read_author(1)
    create_author()
    update_author(4)
    delete_author(4)
    print("Genres")
    read_genres()
    read_genre(1)
    create_genre()
    update_genre(4)
    delete_genre(4)
    print("Books")
    read_books()
    read_book(1)
    create_book()
    update_book(4)
    delete_book(4)
    print("Special Breakpoints")


