# Smart Expense Tracker API

A small REST API for managing personal expenses. It supports adding expenses, listing them, filtering by category, calculating totals, and deleting expenses.

I used FastAPI because it is simple for this size of project and includes interactive OpenAPI/Swagger documentation automatically.

## Features

- Add an expense with title, amount, category, and date
- View all expenses
- Filter expenses by category
- Calculate total expenses overall
- Calculate total expenses by category
- Delete an expense
- Bonus: OpenAPI/Swagger docs at `/docs`

## Project Structure

```text
your-repo/
  README.md
  AI_NOTES.md
  requirements.txt
  src/
    __init__.py
    main.py
  tests/
    test_expenses.py
```

## Install Dependencies

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the Server

```bash
python -m uvicorn src.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
python -m pytest
```

## API Endpoints

### Health Check

```http
GET /
```

### Add Expense

```http
POST /expenses
```

Example body:

```json
{
  "title": "Lunch",
  "amount": 12.5,
  "category": "Food",
  "date": "2026-08-01"
}
```

### View All Expenses

```http
GET /expenses
```

### Filter By Category

```http
GET /expenses?category=Food
```

### Calculate Total

```http
GET /expenses/total
```

### Calculate Total By Category

```http
GET /expenses/total?category=Food
```

### Delete Expense

```http
DELETE /expenses/{expense_id}
```

## Notes

Expenses are stored in memory. Restarting the server clears the list, which is allowed by the assignment because no database is required.
