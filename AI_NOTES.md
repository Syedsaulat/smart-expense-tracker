# AI Notes

I used ChatGPT/Codex to help create the first version of this project and to check that the repository matched the assignment instructions.

## What Was AI-Generated

- The initial FastAPI project structure
- The first version of the API routes in `src/main.py`
- The first version of the pytest test cases in `tests/test_expenses.py`
- Draft README wording and endpoint examples

## What I Reviewed, Validated, Or Changed

- I checked that the project structure matched the required format: `README.md`, `AI_NOTES.md`, `src/`, and `tests/`.
- I verified that each required feature from the assignment had an endpoint:
  - add an expense
  - view all expenses
  - filter expenses by category
  - calculate totals
  - delete an expense
- I ran a manual route-level smoke test for creation, category filtering, overall and category totals, deletion, and the missing-ID error case.
- I reviewed the validation rules, especially that expense amounts must be greater than zero and required string fields cannot be empty.
- I kept the storage in memory because the assignment said a database was not required.
- I added and tested validation that trims whitespace from titles and categories, and rejects values that contain only spaces.
- - After using AI guidance to understand the approach, I added and manually validated whitespace handling for titles and categories, including test cases for blank and trimmed values.
## AI Suggestions I Did Not Use

- I did not add a database because it would make the project more complex than the assignment asked for.
- I did not add authentication because this was outside the required scope.
- I did not add multiple bonus features. I only used FastAPI's built-in OpenAPI/Swagger documentation as the optional bonus.

## My Own Understanding

The API keeps a list of expenses while the server is running. When a new expense is posted, the server creates a unique ID and stores it in the list. The list endpoint can return everything or only expenses matching a category. The total endpoint adds the amounts from the matching expenses. The delete endpoint searches by ID and removes the matching expense if it exists.

## Verification Note

The included `pytest` suite is intended to be run with the command in the README. In my current workspace, the dependency download stalled before I could complete that run, so I have not marked it as completed. The route-level smoke test described above passed using the locally available FastAPI installation.
