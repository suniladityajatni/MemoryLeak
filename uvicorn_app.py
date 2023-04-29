## Fastapi

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    l=[]
    for i in range(1000):
        l.append(i)
    return {"message": "Hello World"}

@app.get("/foo")
async def root():
    r=[]
    for j in range(1000):
        r.append(j**j)
    return {"message": "FOO"}


