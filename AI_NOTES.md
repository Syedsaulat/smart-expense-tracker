# AI Notes

I used ChatGPT to scaffold the project and get a working starting point faster. Here's the breakdown.

## What AI helped with

- Setting up the FastAPI boilerplate — the app instance, Pydantic models, and the basic CRUD route structure in `src/main.py`
- Writing the initial pytest tests in `tests/test_expenses.py`
- Drafting the README layout and the endpoint examples

## What I actually did myself

- Went through every endpoint and made sure it matched what the assignment asked for (add, view, filter, totals, delete). The AI's first pass was close but I had to double-check the category filtering was case-insensitive and that the total endpoint handled the optional category param properly.
- Tested the API manually — I hit each route, checked that creating an expense returned a 201 with the right fields, that filtering by category actually worked with different casing, that deleting a nonexistent ID gave a 404, etc.
- Added a `field_validator` for title and category so that whitespace-only strings like `"   "` get rejected. The AI didn't include this, but I thought it was an obvious edge case that should be handled.
- Added two extra test cases for the whitespace validation (`test_rejects_whitespace_only_title` and `test_trims_title_and_category`).
- Kept the storage in-memory since the assignment said no database was needed. Simpler is better here.

## AI suggestions I skipped

- It suggested adding SQLite — overkill for this, the assignment explicitly says in-memory is fine.
- It offered to add auth middleware — way outside the scope.
- It suggested adding multiple bonus features but the assignment says pick at most one, so I just went with the Swagger docs since FastAPI gives you that basically for free.

## How I understand the code

Basically the app keeps a Python list of expenses in memory. When you POST a new one, it generates a UUID and appends it. The GET endpoint returns the full list or filters by category (case-insensitive). The total endpoint sums up amounts, optionally filtered. Delete finds by ID and pops it, or returns 404. Nothing persists after a restart, which is fine for this assignment.
