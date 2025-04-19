from typing import List
from fastapi import FastAPI, HTTPException, Query, Depends
from sqlmodel import Session, select
from models import *
from database import engine, lifespan, get_session
app = FastAPI(lifespan=lifespan)
@app.get("/")
def home():
    return "Server is running!"

# Authors
@app.get("/authors/",response_model=List[AuthorsPublic])
def read_authors(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        authors = session.exec(select(Authors).offset(offset).limit(limit)).all()
        return authors

@app.get("/authors/{author_id}",response_model=AuthorsPublic)
def read_author(author_id: int):
    with Session(engine) as session:
        author = session.get(Authors, author_id)
        if not author:
            raise HTTPException(status_code=404)
        return author

@app.post("/authors/",response_model=AuthorsPublic)
def create_author(author: AuthorsCreate):
    with Session(engine) as session:
        db_authors = Authors.model_validate(author)
        session.add(db_authors)
        session.commit()
        session.refresh(db_authors)
        return db_authors

@app.patch("/authors/{author_id}",response_model=AuthorsPublic)
def update_author(author_id: int, author: AuthorsUpdate):
    with Session(engine) as session:
        db_author = session.get(Authors, author_id)
        if not db_author:
            raise HTTPException(status_code=404, detail="Author not found")
        author_data = author.model_dump(exclude_unset=True)
        for key, value in author_data.items():
            setattr(db_author, key, value)
        session.add(db_author)
        session.commit()
        session.refresh(db_author)
        return db_author

@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    with Session(engine) as session:
        db_author = session.get(Authors, author_id)
        if not db_author:
            raise HTTPException(status_code=404, detail="Author not found")
        session.delete(db_author)
        session.commit()
        return {f"message":"Deleted" ,"id":{author_id}}

#Genres

@app.get("/genres/",response_model=List[GenresPublic])
def read_genres(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        genres = session.exec(select(Genres).offset(offset).limit(limit)).all()
        return genres

@app.get("/genres/{genre_id}",response_model=GenresPublic)
def read_genre(genre_id: int):
    with Session(engine) as session:
        genre = session.get(Genres, genre_id)
        if not genre:
            raise HTTPException(status_code=404, detail="Genre not found")
        return genre

@app.post("/genres/",response_model=GenresPublic)
def create_genre(genre: GenresCreate):
    with Session(engine) as session:
        db_genre = Genres.model_validate(genre)
        session.add(db_genre)
        session.commit()
        session.refresh(db_genre)
        return db_genre
@app.patch("/genres/{genre_id}",response_model=GenresPublic)
def update_genre(genre_id: int, genre: GenresUpdate):
    with Session(engine) as session:
        db_genre = session.get(Genres, genre_id)
        if not db_genre:
            raise HTTPException(status_code=404, detail="Genre not found")
        genre_data = genre.model_dump(exclude_unset=True)
        for key, value in genre_data.items():
            setattr(db_genre, key, value)
        session.add(db_genre)
        session.commit()
        session.refresh(db_genre)
        return db_genre

@app.delete("/genres/{genre_id}")
def delete_genre(genre_id: int):
    with Session(engine) as session:
        db_genre = session.get(Genres, genre_id)
        if not db_genre:
            raise HTTPException(status_code=404, detail="Genre not found")
        session.delete(db_genre)
        session.commit()
        return {f"message":"Deleted" ,"id":{genre_id}}

#BookGenres
@app.get("/books/",response_model=List[BooksPublic])
def read_books(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        books = session.exec(select(Books).offset(offset).limit(limit)).all()
        return books

@app.get("/book/{book_id}",response_model=BookPublicWithGenres)
def read_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Books, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/",response_model=BooksPublic)
def create_book(book: BooksCreate):
    with Session(engine) as session:
        db_books = Books.model_validate(book)
        session.add(db_books)
        session.commit()
        session.refresh(db_books)
        return db_books

@app.patch("/books/{book_id}",response_model=BooksPublic)
def update_book(book_id: int, book: BooksUpdate):
    with Session(engine) as session:
        db_book = session.get(Books, book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        book_data = book.model_dump(exclude_unset=True)
        for key, value in book_data.items():
            setattr(db_book, key, value)
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    with Session(engine) as session:
        db_book = session.get(Books, book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        session.delete(db_book)
        session.commit()
        return {f"message":"Deleted" ,"id":{book_id}}

# 5 BreakPoints...

# Get Books for genre_id
@app.get("/books/genre/{genre_id}",response_model=GenrePublicWithBooks)
def read_genre(genre_id: int, session: Session = Depends(get_session)):
    genre = session.get(Genres, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

# Get Books by Rating
@app.get("/books/rating/{rating}", response_model=List[BooksPublic])
def read_rating(rating: int, inverse: bool=False, reverse: bool=False, offset: int = 0, limit: int = Query(default=100, le=100)):
#    books_formatted = []
#    with Session(engine) as session:
#        books = session.exec(select(Books).offset(offset).limit(limit)).all()
#        for book in books:
#            if book.rating > rating:
#                books_formatted.append(book)
#        if not books_formatted:
#            raise HTTPException(status_code=404, detail="Book not found")
#        return sorted(books_formatted, key=lambda bo: bo.rating, reverse=reverse)
    with Session(engine) as session:
        if inverse:
            query = select(Books).where(Books.rating < rating).offset(offset).limit(limit)
            if reverse:
                query = query.order_by(Books.rating.desc())
            else:
                query = query.order_by(Books.rating.asc())
        else:
            query = select(Books).where(Books.rating > rating).offset(offset).limit(limit)
            if reverse:
                query = query.order_by(Books.rating.desc())
            else:
                query = query.order_by(Books.rating.asc())
        books = session.exec(query).all()
        if not books:
            raise HTTPException(status_code=404, detail="Book not found")
        return books

# Get books by Name Author
@app.get("/books/author/{name}",response_model=List[BooksPublic])
def get_books_by_name_author(name:str, offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        query = (select(Books).join(Authors, Books.author_id == Authors.id).where(Authors.name.like(f"%{name}%")).offset(offset).limit(limit))
        books = session.exec(query).all()
        if not books:
            raise HTTPException(status_code=404, detail="Book not found")
        return books

# Get Auhtors by Name
@app.get("/authors/age/{age}", response_model=List[AuthorsPublic])
def get_authors_by_age(age: int, inverse: bool=False, reverse: bool=False, offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        if inverse:
            query = select(Authors).where(Authors.age < age).offset(offset).limit(limit)
            if reverse:
                query = query.order_by(Authors.age.desc())
            else:
                query = query.order_by(Authors.age.asc())
        else:
            query = select(Authors).where(Authors.age > age).offset(offset).limit(limit)
            if reverse:
                query = query.order_by(Authors.age.desc())
            else:
                query = query.order_by(Authors.age.asc())
        authors = session.exec(query).all()
        if not authors:
            raise HTTPException(status_code=404, detail="Author not found")
        return authors

# Get books by Title
@app.get("/books/title/{title}",response_model=List[BooksPublic])
def get_books_by_title(title:str, offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        query = (select(Books).where(Books.title.like(f"%{title}%")).offset(offset).limit(limit))
        books = session.exec(query).all()
        if not books:
            raise HTTPException(status_code=404, detail="Book not found")
        return books
