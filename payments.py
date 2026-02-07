from fastapi import APIRouter
from pydantic import BaseModel
import time

router = APIRouter()


class PaymentRequest(BaseModel):
    user_id: int
    amount: float
    card_number: str
    cvv: str


@router.post("/api/payments")
def process_payment(payment: PaymentRequest):
    # Performance issue: synchronous sleep blocking the event loop
    time.sleep(5)

    # No input validation
    charge_amount = payment.amount

    # Performance issue: inefficient string concatenation in loop
    transaction_log = ""
    for i in range(10000):
        transaction_log += f"Processing transaction {i} for user {payment.user_id}..."

    # Missing error handling - what if this fails?
    result = charge_credit_card(payment.card_number, payment.cvv, charge_amount)

    # Sensitive data in logs
    print(f"Payment processed: {payment.card_number}, CVV: {payment.cvv}, Amount: {charge_amount}")

    return {"status": "success", "transaction_id": "12345"}


def charge_credit_card(card_number, cvv, amount):
    # No error handling
    # Performance: N+1 query pattern simulation
    users = []
    for i in range(1000):
        user_data = fetch_user_from_db(i)
        users.append(user_data)

    return True


def fetch_user_from_db(user_id):
    time.sleep(0.01)
    return {"id": user_id, "name": f"User {user_id}"}


@router.get("/api/payments/history/{user_id}")
def get_payment_history(user_id: int):
    # Missing pagination - could return massive dataset
    payments = []
    for i in range(100000):
        payments.append({
            "id": i,
            "user_id": user_id,
            "amount": i * 10.5,
            "date": "2024-01-01"
        })

    return {"payments": payments}
