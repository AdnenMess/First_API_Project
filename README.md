## FastAPI


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
