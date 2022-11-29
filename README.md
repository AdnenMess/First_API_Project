# FastAPI


We have to install `fastapi` and `uvicorn(light web server)`

```shell
pip install fastapi
pip install uvicorn
```
***

1-  **A Minimal API endpoint**

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

