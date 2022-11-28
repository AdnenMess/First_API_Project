from fastapi import FastAPI
import uvicorn

api = FastAPI()


@api.get('/api/calculate')
def calculate():
    value = 2+2
    result = {'result': value}
    return result


uvicorn.run(api, port=8001, host="127.0.0.2")
