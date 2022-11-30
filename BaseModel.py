from _datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

order_json = {
    'item_id': '123',
    'created_date': '2022-11-29 12:10',
    'pages_visited': [1, 2, '3'],
    'price': 17.22}


class Order(BaseModel):
    item_id: int
    created_date: Optional[datetime]
    pages_visited: List[int] = []
    price: float


order = Order(**order_json)
print(order)
