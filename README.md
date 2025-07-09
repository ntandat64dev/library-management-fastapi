# Library Management FastAPI

FastAPI application for managing books in a library.

## Requirements

- Any library member should be able to search books by their title, author, subject category as well by the publication date.
- There could be more than one copy of a book, and library members should be able to check-out and reserve any copy.
- The system should be able to retrieve information like who took a particular book or what are the books checked-out by a specific library member.
- There should be a maximum limit (5) on how many books a member can check-out.
- There should be a maximum limit (10) on how many days a member can keep a book.
- The system should be able to collect fines for books returned after the due date.
- Members should be able to reserve books that are not currently available.
- The system should be able to send notifications whenever the reserved books become available, as well as when the book is not returned within the due date.
- Each book and member card will have a unique barcode. The system will be able to read barcodes from books and members' library cards.

## Use cases

### Member

- Register new account.
- View pagination list of books.
- Search books by ISBN, title, author, subject, pushlish date range.
- View book detail information.
- Borrow book
  - From book detail page.
  - Choose borrow date, returned date.

### System

- Calculate fine when members loan books.

### Librarian

- Add new book. (book management)
- Update book info. (book management)
- Delete book. (book management)
- Update loans status when member returns books. (loans management)

## Database Schema

All table must includes **audit fields**.

- `book`:

  - id: uuid
  - isbn: str
  - title: str
  - author: str
  - publisher: str
  - publication_date: date
  - genre_id: uuid
  - language: str (language code as ISO 639-1)
  - dimension: str (widthxthickxheight format, e.g., 1.2x1.8x1.7)
  - total_copies: number
  - available_copies: number

- `genre`:

  - id: uuid
  - name: str

- `loan`:

  - id: uuid
  - book_id: uuid
  - member_id: uuid
  - loan_date: date
  - due_date: date
  - fine_amount: number
  - status: enum('BORROWED', 'RETURNED', 'OVERDUE')

- `account`:

  - id: uuid
  - usename: str
  - hashed_password: str

- `member`:

  - id: uuid
  - full_name: str
  - email: str
  - account_id: uuid
  - membership_status: enum('ACTIVE', 'INACTIVE')

- `librarian`:

  - id: uuid
  - full_name: str
  - email: str
  - acount_id: uuid

## APIs

### Librarian

- POST `/api/books` # add new book
- PUT `/api/books/:id` # update book
- DELETE `/api/books/:id` # delete book
- PUT `/api/loans/:id` # update loan status

### Member

- GET `/api/books` # get all books
- GET `/api/books/:id` # get book by id
- POST `/api/loans` # create a loan
