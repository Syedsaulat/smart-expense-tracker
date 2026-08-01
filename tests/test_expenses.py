from fastapi.testclient import TestClient

from src.main import app, expenses


client = TestClient(app)


def setup_function():
    expenses.clear()


def sample_expense(title="Lunch", amount=12.50, category="Food", date="2026-08-01"):
    return {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date,
    }


def test_add_expense():
    response = client.post("/expenses", json=sample_expense())

    assert response.status_code == 201
    data = response.json()
    assert data["id"]
    assert data["title"] == "Lunch"
    assert data["amount"] == 12.50
    assert data["category"] == "Food"


def test_view_all_expenses():
    client.post("/expenses", json=sample_expense(title="Lunch", category="Food"))
    client.post("/expenses", json=sample_expense(title="Bus", amount=3.25, category="Travel"))

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_filter_expenses_by_category():
    client.post("/expenses", json=sample_expense(title="Lunch", category="Food"))
    client.post("/expenses", json=sample_expense(title="Bus", amount=3.25, category="Travel"))

    response = client.get("/expenses?category=food")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Lunch"


def test_calculate_total_overall():
    client.post("/expenses", json=sample_expense(amount=10, category="Food"))
    client.post("/expenses", json=sample_expense(title="Taxi", amount=7.75, category="Travel"))

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json() == {"total": 17.75, "category": None}


def test_calculate_total_by_category():
    client.post("/expenses", json=sample_expense(amount=10, category="Food"))
    client.post("/expenses", json=sample_expense(title="Taxi", amount=7.75, category="Travel"))

    response = client.get("/expenses/total?category=Food")

    assert response.status_code == 200
    assert response.json() == {"total": 10.0, "category": "Food"}


def test_delete_expense():
    create_response = client.post("/expenses", json=sample_expense())
    expense_id = create_response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")
    list_response = client.get("/expenses")

    assert delete_response.status_code == 204
    assert list_response.json() == []


def test_delete_missing_expense_returns_404():
    response = client.delete("/expenses/not-a-real-id")

    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found"


def test_rejects_negative_amount():
    response = client.post("/expenses", json=sample_expense(amount=-5))

    assert response.status_code == 422
    
def test_rejects_whitespace_only_title():
    response = client.post("/expenses", json=sample_expense(title="   "))

    assert response.status_code == 422


def test_trims_title_and_category():
    response = client.post(
        "/expenses",
        json=sample_expense(title="  Lunch  ", category="  Food  "),
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Lunch"
    assert response.json()["category"] == "Food"