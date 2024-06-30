from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def index_get(request: Request):
    return f"{request.client.host}: Hello world!"


if __name__ == '__main__':
    uvicorn.run(app, reload=True, host="0.0.0.0", port=8000)
