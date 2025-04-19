from symtable import Class
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

# Authors
class AuthorsBase(SQLModel):
    name: str = Field(index=True)
    age: int = Field(index=True)
    description: str = Field(index=True)

class Authors(AuthorsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class AuthorsCreate(AuthorsBase):
    pass

class AuthorsPublic(AuthorsBase):
    id: int

class AuthorsUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
    description: Optional[str] = None

#BookGenres
class BookGenres(SQLModel, table=True):
    book_id: int  = Field(index=True, foreign_key="books.id", primary_key=True)
    genre_id: int = Field(index=True, foreign_key="genres.id", primary_key=True)


# Genres
class GenresBase(SQLModel):
    name: str = Field(index=True)
    description: str = Field(index=True)

class Genres(GenresBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    books : list["Books"] = Relationship(
        back_populates="genres",
        link_model=BookGenres,
    )

class GenresCreate(GenresBase):
    pass

class GenresPublic(GenresBase):
    id : int

class GenresUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None


#Books
class BooksBase(SQLModel):
    title: str = Field(index=True)
    description: str = Field(index=True)
    rating: int = Field(default=None, index=True)
    author_id: Optional[int] =Field(default=None, foreign_key="authors.id")

class Books(BooksBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author: Optional["Authors"] = Relationship()
    genres: list["Genres"] = Relationship(
        back_populates="books",
        link_model=BookGenres
    )

class BooksCreate(BooksBase):
    pass

class BooksPublic(BooksBase):
    id : int

class BooksUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[int] = None

class BookPublicWithGenres(BooksPublic):
    genres: list[GenresPublic] = None

class GenrePublicWithBooks(GenresPublic):
    books: list[BooksPublic] = None

