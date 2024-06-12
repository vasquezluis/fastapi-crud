from fastapi import FastAPI

# instance of fastapi
app = FastAPI()


# basic route
@app.get("/")
def read():
    return {"hello": "world"}


# execute the api
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
