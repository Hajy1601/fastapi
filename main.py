from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()



@app.get('/')
def home():
    a = requests.get('http://178.20.45.13:8000/ru/product/get/all')
    b = a.json()
    return b

print("CHLEEEN")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",   # файл:переменная
        host="0.0.0.0",
        port=8000,
        reload=True   # авто-перезапуск при изменениях (для разработки)
    )