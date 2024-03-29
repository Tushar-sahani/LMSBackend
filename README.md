# Library Management System API

This API allows you to manage books in a library.

## Endpoints

- **GET /api/books/**: Retrieve a list of all books.
- **POST /api/books/add/**: Add a new book.
  - Request body should be a JSON object with the following fields: `title`, `authors`, `publication_date`, `isbn`, `description`.
- **GET /api/books/<str:isbn>/**: Retrieve a book by ISBN.
- **PUT /api/books/update/<str:isbn>/**: Update a book by ISBN.
  - Request body should be a JSON object with the fields you want to update: `title`, `authors`, `publication_date`, `description`.
- **DELETE /api/books/delete/<str:isbn>/**: Delete a book by ISBN.

## Usage

1. Clone the repository:

   ```sh
   git clone https://github.com/your_username/your_repo.git

2. Install dependencies:

   ```sh
   pip install -r requirements.txt

3. Run the development server:

   ```sh
   python manage.py runserver

4. Access the API at http://localhost:8000/api/books/.

## Example
To add a new book, send a POST request to /api/books/ with the following JSON payload:
```JSON
  {
  "title": "Example Book",
  "authors": "John Doe",
  "publication_date": "2022-01-01",
  "isbn": "1234567890",
  "description": "An example book description."
  }
