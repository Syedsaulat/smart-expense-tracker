from datetime import date
from typing import List, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A small REST API for tracking personal expenses.",
    version="1.0.0",
)


class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=50)
    date: date

    @field_validator("title", "category")
    @classmethod
    def clean_required_text(cls, value: str) -> str:
        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("must not be blank")

        return cleaned_value

class Expense(ExpenseCreate):
    id: str


class TotalResponse(BaseModel):
    total: float
    category: Optional[str] = None


expenses: List[Expense] = []


@app.get("/")
def health_check():
    return {"message": "Smart Expense Tracker API is running"}


@app.post("/expenses", response_model=Expense, status_code=status.HTTP_201_CREATED)
def add_expense(expense_data: ExpenseCreate):
    expense = Expense(id=str(uuid4()), **expense_data.model_dump())
    expenses.append(expense)
    return expense


@app.get("/expenses", response_model=List[Expense])
def view_expenses(category: Optional[str] = None):
    if category is None:
        return expenses

    return [
        expense
        for expense in expenses
        if expense.category.lower() == category.lower()
    ]


@app.get("/expenses/total", response_model=TotalResponse)
def calculate_total(category: Optional[str] = None):
    matching_expenses = view_expenses(category)
    total = round(sum(expense.amount for expense in matching_expenses), 2)
    return TotalResponse(total=total, category=category)


@app.delete("/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: str):
    for index, expense in enumerate(expenses):
        if expense.id == expense_id:
            expenses.pop(index)
            return None

    raise HTTPException(status_code=404, detail="Expense not found")