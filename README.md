class ValidationError:
pass# FastAPI


We have to install `fastapi` and `uvicorn(light web server)`

```shell
pip install fastapi
pip install uvicorn
```

Then we have to install `BaselModel` from the library  `pydantic` (validation data modeling)

```shell
pip install pydandic
```

***

1- **A Minimal API endpoint**

```python
from fastapi import FastAPI
import uvicorn

api = FastAPI()


@api.get('/api/calculate')
def calculate():
    return 2 + 2

uvicorn.run(api, host="127.0.0.1", port=8000)
```

***

2- **Retuning errors**

```python
import fastapi
from typing import Optional

api = fastapi.FastAPI()

@api.get('/api/calculate')
def calculate(x: int,y: int,z : Optional[int] = None):
    error_dict = {'error' : 'z cannot be zero'}
    if z is not None and z == 0:
        return fastapi.responses.JSONResponse(
                       status_code=400, content=error_dict)
    result = x + y
    if z is not None:
        result /= z
    return result
```

***

3- **type-hints**

```python
from typing import Iterable, Optional
from collections import namedtuple

Item = namedtuple("Item", "name, value")

running_max: Optional[int] = None

def counter(items: Iterable[Item]) -> int:
    total = 0
    for i in items:
        total += i.value
    return total
```
***

4- **Asynchronous programming**

```python
# ASGI (Asynchronous Server Gateway Interface)
async def app(scope, receive, send):
    r = await receive(scope)
    return await send(r, scope)
```
***

5- **BaseModel**

```python
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class Order(BaseModel):
    item_id: int    
    create_date: datetime
    price: float
    pages_visited: Optional[List[int]] = []

    
order_json = {
    'item_id': '123',
    'created_date': '2022-11-29 12:10',
    'pages_visited': [1, 2, '3'],
    'price': 17.22}

order = Order(**order_json)
```

***

6- **Build 'real' apps**

```python
import fastapi
from api import weather_api
from views import home

router = fastapi.APIRouter()

# api/weather_api.py
@router.get('/api/weather')
def weather():
    return 'Function of weather-API'
   
# views/home.py
@router.get('/', include_in_schema=False)
def home():
    return {'name': 'Micheal'}

# main.py
app = fastapi.FastAPI()
app.include_router(weather_api.router)
app.include_router(home.router)
```

***

7- **Calling an external API asynchronously**

```python
import httpx
from typing import Optional

api_key = "secret_key"

async def get_report_async(city: str, country: Optional[str], 
                           state: Optional[str], units: str) -> dict :
    q = f"{city}, {state}, {country}"
    url = f"https://api.openwathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"

    async with httpx.AsyncClient() as client:
        r: httpx.Response = await client.get(url)
        if r.status_code != 200:
            raise ValidationError(status_code=r.status_code, error_msg=r.text)

        data = r.json()
        forecast = data['main']
        return forecast

```

***


