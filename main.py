from fastapi import FastAPI
from pydantic import BaseModel

from datetime import datetime

app = FastAPI()

# We create a Coffee class model with attibutes that we want to use
class Coffee(BaseModel):
    order_id: int
    order_date: datetime
    coffee_type: str
    coffee_price: float
    
# We use type hints for coffee_list
coffees_list : list[Coffee] = [
    Coffee(
        order_id= 1,
        order_date= datetime.now(),
        coffee_type="Mocaccino",
        coffee_price= 2.5
    )
]



@app.get("/")
def get_message():
    return {
        "message": "Welcome to Coffee Shop API!"
    }


@app.get("/coffees")
def get_coffees() -> list[Coffee]:
    return coffees_list