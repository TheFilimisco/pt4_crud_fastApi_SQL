from sqlmodel import Session

from models import Authors, Genres, Books, BookGenres
from database import engine, create_db


def create_sample():
    with Session(engine) as session:
        # Genres
        genre_horror = Genres(name="Horror", description="Scaring, Thrillers and Creep")
        genre_adventure = Genres(name="Adventure", description="Adventure, explorer and missions")
        genre_romance  = Genres(name="Romance", description="Loves and Romance")

        session.add(genre_horror)
        session.add(genre_adventure)
        session.add(genre_romance)
        session.commit()

        session.refresh(genre_horror)
        session.refresh(genre_adventure)
        session.refresh(genre_romance)

        print("Created genre: ", genre_horror)
        print("Created genre: ", genre_adventure)
        print("Created genre: ", genre_romance)

        # Authors
        author_stephen = Authors(name="Stephen King", age=43, description="Born on USA is Writer... ")
        author_ernesto = Authors(name="Enesto Sabato", age=35, description="Born on Venezuela is Writer... ")
        author_lewis = Authors(name="Lewis Carroll", age=45, description="Lewis Carroll, was an English author, poet, mathematician, photographer ")

        session.add(author_stephen)
        session.add(author_ernesto)
        session.add(author_lewis)
        session.commit()

        session.refresh(author_stephen)
        session.refresh(author_ernesto)
        session.refresh(author_lewis)

        print("Created author: ", author_stephen)
        print("Created author: ", author_ernesto)
        print("Created author: ", author_lewis)

        #Books
        book_alice = Books(title="Alice's Adventures in Wonderland", description="It details the story of a girl named Alice who falls through a rabbit hole into a fantasy world of anthropomorphic creatures.", rating=2, author=author_lewis)
        book_it = Books(title= "It", description=" A band of seven uncool 11-year-olds, led by Bill Denbrough, discovers and battles an evil, shape-changing monster that the children call It.", rating=2, author=author_stephen)
        book_tunel = Books(title="The Tunnel", description="Is framed as the confession of the painter Juan Pablo Castel, who has murdered the only woman capable of understanding him", rating=6, author=author_ernesto)

        #BookGenres
        book_alice.genres.append(genre_adventure)
        book_alice.genres.append(genre_romance)
        book_it.genres.append(genre_horror)
        book_tunel.genres.append(genre_adventure)

        session.add(book_alice)
        session.add(book_it)
        session.add(book_tunel)

        session.commit()

        session.refresh(book_alice)
        session.refresh(book_it)
        session.refresh(book_tunel)

        print("Created book: ", book_alice)
        print("Created book: ", book_it)
        print("Created book: ", book_tunel)


def main():
    create_db()
    create_sample()

if __name__ == '__main__':
    main()